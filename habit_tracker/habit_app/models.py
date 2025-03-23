from django.db import models
from django.conf import settings


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

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)
    name = models.CharField(max_length=250)
    description = models.TextField()
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
    

