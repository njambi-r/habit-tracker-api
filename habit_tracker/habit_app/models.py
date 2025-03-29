from django.db import models
from django.conf import settings
import datetime

# Create your models here.
class Habit(models.Model):
    # Select the frequency
    FREQUENCY_CHOICES = [
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly')
    ]

    #Select if completed or active
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Completed', 'Completed')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    name = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    frequency = models.CharField(
        max_length=20, 
        choices=FREQUENCY_CHOICES, 
        default='Daily')
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='Active')
    completed_at = models.DateTimeField(null=True, blank=True)

    """Automatically set the datetime when a habit is marked as complete"""
    def save(self, *args, **kwargs):
        if self.status == 'Completed' and not self.completed_at:
            self.completed_at = datetime.now()
        elif self.status == 'Active':
            self.completed_at = None
        super().save(*args, **kwargs)
    

