from .models import ActivityLog  # Import the ActivityLog model to log actions

def log_activity(action, user=None, details=None):
    # Save an activity log entry with action, user, and details
    ActivityLog.objects.create(action=action, user=user, details=details)
