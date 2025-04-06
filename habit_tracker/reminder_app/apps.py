from django.apps import AppConfig


class ReminderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reminder_app'

    def ready(self):
        import reminder_app.signals  # This connects the signal when the app is ready
