"""
URL configuration for habit_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user_app.urls')), # user app
    path('api-auth/', include('rest_framework.urls')),  # Optional: Browsable API login/logout
    path('api/', include('habit_app.urls')), # habit app
    path('api/', include('analytics_app.urls')), # analytics app
    path('api/', include('reminder_app.urls')), # analytics app

]

#----------------------------------------------
# Add interactive Swagger documentation
# visit http://127.0.0.1:8000/swagger/ to explore the API
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="HABIT TRACKER API",
        default_version='v1',
        description="API for tracking habits",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
