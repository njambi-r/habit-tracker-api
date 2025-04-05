from django.db import models
from habit_app.models import Habit

# Create your models here.
class HabitAnalytics(models.Model):
    habit = models.OneToOneField(Habit, on_delete=models.CASCADE, related_name='analytics')
    total_completions = models.PositiveIntegerField(default=0)
    average_completion_time = models.DurationField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)