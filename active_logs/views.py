from active_logs.utils import log_activity
from django.http import JsonResponse
from .models import ActivityLog

def create_task(request):
    # Your logic for creating a task
    ...
    log_activity(action="Created Task", user=request.user.username, details="Task ID: 123")


def get_activity_logs(request):
    logs = ActivityLog.objects.all().order_by('-timestamp').values('action', 'user', 'timestamp', 'details')
    return JsonResponse(list(logs), safe=False)
