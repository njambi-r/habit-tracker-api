from rest_framework import serializers
from .models import Habit
import datetime
from reminder_app.serializer import ReminderSerializer
from analytics_app.serializer import HabitAnalyticsSerializer

class HabitSerializer(serializers.ModelSerializer):
    reminders = ReminderSerializer(many=True, read_only=True)
    analytics = HabitAnalyticsSerializer(read_only=True)
    
    class Meta:
        model = Habit
        fields = '__all__' #fields to include in the api response
        read_only_fields = ['user','created_at', 'completed_at']

    """Ensure user cannot set start dates in the past"""
    def validate_start_date(self, value):
        if value < datetime.date.today():
            raise serializers.ValidationError("Start date must be in the future.")
        return value
        