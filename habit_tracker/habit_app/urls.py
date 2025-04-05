from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HabitViewSet, HabitFilterView

router = DefaultRouter()
router.register(r'habits', HabitViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Includes all routes from the router
    path('filter-habits/', HabitFilterView.as_view(), name='habit-filter'),  # filtering endpoint
]
