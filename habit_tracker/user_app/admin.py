from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
# Registering the custom user model
# https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#specifying-custom-user-model:~:text=your%20user%20model.-,Using%20a%20custom%20user%20model%20when%20starting%20a%20project,-%C2%B6
admin.site.register(User, UserAdmin)