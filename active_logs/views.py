from active_logs.utils import log_activity  # Importing a utility to log activities
from django.http import JsonResponse       # Importing JsonResponse to return data in JSON format
from .models import ActivityLog            # Importing the ActivityLog model to interact with the database

def create_task(request):
    # Logic for creating a task (specifics depend on your application's needs)
    ...
    # Logging the task creation activity with relevant details
    log_activity(action="Created Task", user=request.user.username, details="Task ID: 123")


def get_activity_logs(request):
    # Fetch all activity logs from the database, sorted by the newest entries first
    logs = ActivityLog.objects.all().order_by('-timestamp').values('action', 'user', 'timestamp', 'details')
    # Return the logs as a JSON response, converting the queryset to a list
    return JsonResponse(list(logs), safe=False)
