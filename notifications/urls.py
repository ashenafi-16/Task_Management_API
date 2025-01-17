from django.urls import path  # Importing path to define URL routes
from .views import send_task_reminder, NotificationDeleteView  # Importing views for task reminder and notification deletion

urlpatterns = [
    path('reminder/<int:task_id>/', send_task_reminder, name='send_task_reminder'),  # URL to send a task reminder
    path('notifications/<int:pk>/', NotificationDeleteView.as_view(), name='notification-delete'),  # URL to delete a specific notification
]
