from django.db import models
from habit_app.models import Habit

# Create your models here.
class HabitAnalytics(models.Model):
    habit = models.OneToOneField(Habit, on_delete=models.CASCADE, related_name='analytics')
    total_completions = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    #Add fields for streak
    current_streak = models.PositiveIntegerField(default=0)
    longest_streak = models.PositiveIntegerField(default=0)
    last_completed_date = models.DateField(null=True, blank=True)