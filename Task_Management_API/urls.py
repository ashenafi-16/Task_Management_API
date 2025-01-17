"""
URL configuration for Task_Management_API project.

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
from django.urls import path, include  # Importing path and include to define URL routing

urlpatterns = [
    path('', include('user_account.urls')),  # Include URLs from the user_account app for user-related views
    path('admin/', admin.site.urls),  # URL for the Django admin site
    path('api/', include('tasks.urls')),  # Include URLs from the tasks app for task-related API endpoints
    path('api/', include('catagories.urls')),  # Include URLs from the categories app for category-related API endpoints
    path('api/', include('notifications.urls')),  # Include URLs from the notifications app for notification-related API endpoints
    path('api/', include('active_logs.urls')),  # Include URLs from the active_logs app for logging-related API endpoints
    path('', include('task_manager.urls')),  # Include URLs from the task_manager app for general task management views
]
