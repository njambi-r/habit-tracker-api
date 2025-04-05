from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HabitAnalyticsViewSet

router = DefaultRouter()
router.register(r'analytics', HabitAnalyticsViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Includes all routes from the router
]