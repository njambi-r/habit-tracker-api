from django.shortcuts import render
from rest_framework import viewsets
from .models import Reminder
from .serializers import ReminderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from habit_app.models import Habit
from rest_framework.exceptions import ValidationError

# Create your views here.
class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(habit__user=self.request.user)

    #ensure created reminder is tied to an existing habit that is active and not closed
    def perform_create(self, serializer):
        habit_id = self.request.data.get('habit')
        
        if habit_id:
            # Ensure the habit exists and belongs to the current user
            habit_instance = Habit.objects.filter(id=habit_id, user=self.request.user).first()
            
            if not habit_instance:
                raise ValidationError({"habit": "Invalid habit or habit does not belong to the current user."})
            
            # Ensure the habit's status is "Active"
            if habit_instance.status != "Active":
                raise ValidationError({"habit": "The habit must be active to create a reminder."})

            # Associate habit with the reminder and save
            serializer.save(habit=habit_instance)
        else:
            # Optional: Raise error if habit is not provided
            raise ValidationError({"habit": "Habit must be specified."})
        
    #Activate and deactivate reminder
    @action(detail=True, methods=['patch'])
    def deactivate_reminder(self, request, pk=None):
        reminder = self.get_object()
        if reminder.is_active == False:
            return Response({"message": "Reminder is already inactive."})
        reminder.is_active = False
        reminder.save()
        return Response({"message": "Reminder deactivated successfully."})

    @action(detail=True, methods=['patch'])
    def activate_reminder(self, request, pk=None):
        reminder = self.get_object()
        if reminder.is_active == True:
            return Response({"message": "Reminder is already active."})
        reminder.is_active = True
        reminder.save()
        return Response({"message": "Reminder activated successfully."})
