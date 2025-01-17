from django.db import models

class ActivityLog(models.Model):
    action = models.CharField(max_length=255)  # e.g., "Created Task", "Deleted Task"
    user = models.CharField(max_length=255, null=True, blank=True)  # User responsible for the action
    timestamp = models.DateTimeField(auto_now_add=True)  # When the action occurred
    details = models.TextField(null=True, blank=True)  # Optional details about the action

    def __str__(self):
        return f"{self.action} by {self.user or 'System'} on {self.timestamp}"
