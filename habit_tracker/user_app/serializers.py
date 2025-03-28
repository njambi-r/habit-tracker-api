from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#django.contrib.auth.get_user_model:~:text=as%20described%20below.-,Referencing%20the%20User%20model,-%C2%B6 
"""
Since the AUTH_USER_MODEL setting has been changed to a 
different user model, it is referenced using django.contrib.auth.get_user_model().
This method will return the currently active user model - 
the custom user model if one is specified, or User otherwise.
"""
User = get_user_model()

# user model serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email', 'password','bio','profile_picture']
        extra_kwargs = {'password': {'write_only': True}} #This prevents the password from being included in API responses.

# serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email', 'password'] # fields provided by users when registering
        extra_kwargs = {'password': {'write_only': True}} #This prevents the password from being included in API responses.

    # method called when serializer.save() is executed
    # it receives validated_data -- which is cleaned up user input
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) # Django’s built-in create_user() method to create a new user
        token, created = Token.objects.get_or_create(user=user)
        """
        If the user is newly created, a token is generated for them.
        If the user already exists, their existing token is retrieved.
        """
        return user 