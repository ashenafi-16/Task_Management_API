from django.db import models  # Importing Django's models module
from django.contrib.auth.models import User  # Importing the User model to link notifications with users
from tasks.models import Task  # Importing the Task model to link notifications with tasks

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link notification to a specific user
    task = models.ForeignKey(Task, on_delete=models.CASCADE)  # Link notification to a specific task
    message = models.TextField()  # Message content for the notification
    is_read = models.BooleanField(default=False)  # Flag to indicate if the notification has been read
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the notification was created

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message[:20]}"  # Display a short preview of the message
