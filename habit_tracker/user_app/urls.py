from django.urls import path
from .views import RegisterView, LoginView, ProfileView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', ObtainAuthToken.as_view(), name='api-login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
