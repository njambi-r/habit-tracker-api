from django.db import models
from django.contrib.auth.models import AbstractUser

"""
Setting up a custom user that behaves like the default user model
just in case we need to customize it later. 
https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#specifying-custom-user-model:~:text=your%20user%20model.-,Using%20a%20custom%20user%20model%20when%20starting%20a%20project,-%C2%B6 
"""
class User(AbstractUser):
    pass #Keep it identical to Django's default User for now

