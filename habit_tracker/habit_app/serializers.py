from rest_framework import serializers
from .models import Habit
import datetime

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__' #fields to include in the api response
        read_only_fields = ['user','created_at', 'completed_at']

    """Ensure user cannot set start dates in the past"""
    def validate_start_date(self, value):
        if value < datetime.datetime.now():
            raise serializers.ValidationError("Start date must be in the future.")
        return value
        