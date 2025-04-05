from rest_framework import serializers
from .models import HabitAnalytics

class HabitAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitAnalytics
        fields = '__all__'