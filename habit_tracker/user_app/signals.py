# https://www.django-rest-framework.org/api-guide/authentication/#obtaining-auth-tokens:~:text=over%20https.-,Generating%20Tokens,-By%20using%20signals
# Automatically generate a token for every user

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)