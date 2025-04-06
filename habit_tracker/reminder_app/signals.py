from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Reminder
from habit_app.models import Habit


@receiver(post_save, sender=Habit)
def update_reminders_on_habit_status_change(sender, instance, **kwargs):
    # Check if the habit has been closed
    if instance.status == 'Closed':
        # Update related reminders to inactive
        Reminder.objects.filter(habit=instance).update(is_active=False)  # related reminder set to inactive
