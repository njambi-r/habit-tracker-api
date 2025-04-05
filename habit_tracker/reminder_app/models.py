from django.db import models
from habit_app.models import Habit

# Create your models here.
class Reminder(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='reminders')
    time = models.TimeField()
    message = models.CharField(max_length=255, default='Time to do your habit!')
    repeat = models.CharField(max_length=20, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')])
    created_at = models.DateTimeField(auto_now_add=True)

