from django.shortcuts import render
from rest_framework import viewsets
from .models import Reminder
from .serializers import ReminderSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(habit__user=self.request.user)
