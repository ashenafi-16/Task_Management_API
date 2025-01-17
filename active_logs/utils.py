from .models import ActivityLog

def log_activity(action, user=None, details=None):
    ActivityLog.objects.create(action=action, user=user, details=details)
