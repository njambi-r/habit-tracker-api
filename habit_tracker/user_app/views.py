from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework .views import APIView
from rest_framework import generics, permissions
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework.authentication import TokenAuthentication

User = get_user_model()

# user registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=request.data['username'])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})

# User Login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            update_last_login(None, user)
            return Response({"token": token.key})
        return Response({"error": "Invalid Credentials"}, status=400)

# User Profile View
class ProfileView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
