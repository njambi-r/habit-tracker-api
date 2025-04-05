from django.shortcuts import render
from rest_framework import viewsets
from .models import HabitAnalytics
from .serializers import HabitAnalyticsSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class HabitAnalyticsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HabitAnalytics.objects.all()
    serializer_class = HabitAnalyticsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(habit__user=self.request.user)