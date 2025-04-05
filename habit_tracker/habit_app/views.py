from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from .models import Habit
from .serializers import HabitSerializer
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from datetime import datetime
from rest_framework.pagination import PageNumberPagination

# Create your views here.
# Add pagination to support page numbers as query parameters
# for habit search and filter 
class HabitPagination(PageNumberPagination):
    page_size = 10 #items/pg. if not specified, Defaults to `None`, meaning pagination is disabled. 
    page_size_query_param = 'page_size' #Default is 'None'. Set to eg 'page_size' to enable usage.
    max_page_size = 50 #Max page size a client can request. Only relevant if 'page_size_query_param' has also been set.


# setup CRUD operations for habits
class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = HabitPagination #enable pagination
    """
    https://www.django-rest-framework.org/api-guide/permissions/#isauthenticated 
    Deny permission to any unauthenticated user. API only accessible to registered users. 
    """
    # Add habit filtering, search, and sorting
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['status', 'start_date', 'completed_at', 'frequency']
    search_fields = ['name', 'description', 'status']
    ordering_fields = ['name', 'created_at', 'start_date', 'completed_at', 'status', 'frequency']

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)   
    """ensure logged in user can only see their data"""

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 
    """
    Assign a new habit to the logged in user
    https://stackoverflow.com/questions/41094013/when-to-use-serializers-create-and-modelviewsets-perform-create
    perform_create is used when you want to supply 
    extra data before save (like serializer.save(owner=self.request.user) 
    """
    
    # https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions:~:text=URL%20configuration%20throughout.-,ViewSet%20actions,-The%20default%20routers
    """
    Adjust viewset behaviour based on the current action
    Action when user marks a habit as completed
    """
    @action(detail=True, methods=['patch'])
    def mark_complete(self, request, pk=None):
        habit = self.get_object()
        if habit.status == 'Completed':
            return Response({'message': 'Habit is already completed.'}, status=400)
        habit.status = 'Completed'
        habit.save()
        return Response({'message': 'Habit marked as complete.'})

    """
    Action when user wants to reactivate a habit they already completed in the past
    A new instance of the habit will be created instead.
    The habit will be duplicated as opposed to marking it as active to retain records
    """
    @action(detail=True, methods=['patch'])
    def reactivate_habit(self, request, pk=None):
        habit = self.get_object()

        if habit.status != 'Completed':
            return Response({'message': 'Only completed habits can be reactivated.'}, status=400)

        # Validate start_date
        start_date = request.data.get('start_date', None)
        if start_date:
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
                if start_date < datetime.now().date():
                    return Response({'message': 'Start date must be today or in the future.'}, status=status.HTTP_400_BAD_REQUEST)
            except ValueError:
                return Response({'message': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            start_date = datetime.now()
            
            # Create a new habit instance
            new_habit = Habit.objects.create(
                user=request.user,
                name=habit.name,  # Copy name
                description=habit.description,  # Pre-filled but editable
                created_at=datetime.now(),  # Reflect the reactivation timestamp
                start_date=start_date,  # User-defined start date or default now
                frequency=habit.frequency,  # Pre-filled but editable
                status="Active",  # Reset to Active
                completed_at=None  # Ensure it's not marked as completed
            )

            return Response({
                'message': 'Habit reactivated successfully as a new occurrence.',
                'new_habit_id': new_habit.id
            }, status=status.HTTP_201_CREATED)
        



