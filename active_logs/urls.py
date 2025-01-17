from django.urls import path
from .views import get_activity_logs

# Setting up the URL patterns for this app
# The 'activity/logs/' URL is linked to the 'get_activity_logs' view function
urlpatterns = [
    path('activity/logs/', get_activity_logs, name='get_activity_logs'),
]
