from django.urls import path
from .views import send_task_reminder, NotificationDeleteView  # Make sure the view name is correct

urlpatterns = [
    path('reminder/<int:task_id>/', send_task_reminder, name='send_task_reminder'),
    path('notifications/<int:pk>/', NotificationDeleteView.as_view(), name='notification-delete'),  # Corrected name
]
