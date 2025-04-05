# Generated by Django 5.1.7 on 2025-04-05 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('habit_app', '0004_habit_current_streak_habit_last_completed_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HabitAnalytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_completions', models.PositiveIntegerField(default=0)),
                ('average_completion_time', models.DurationField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('habit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='analytics', to='habit_app.habit')),
            ],
        ),
    ]
