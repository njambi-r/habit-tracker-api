from django.db import models
from habit_app.models import Habit
from django.utils import timezone

# Create your models here.
class Reminder(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='reminders')
    time = models.TimeField()
    message = models.CharField(max_length=255, default="It's time!") # Message for the reminder
    repeat = models.CharField(max_length=20, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')])
    is_active = models.BooleanField(default=True) # Whether the reminder is active or inactive
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reminder for {self.habit.name} at {self.reminder_time}"

    def is_due(self):
        # Check if the reminder time has passed and is still active
        return self.reminder_time <= timezone.now() and self.is_active

