from django.urls import path
from .views import get_activity_logs

urlpatterns = [
    path('activity/logs/', get_activity_logs, name='get_activity_logs'),
]
