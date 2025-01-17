from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from tasks.models import Task
from .models import Notification
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

@api_view(['POST'])
def send_task_reminder(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    if task.due_date:
        time_remaining = task.due_date - timezone.now()
        if time_remaining.total_seconds() <= 86400:  # 24 hours in seconds
            Notification.objects.create(
                user=task.user,
                task=task,
                message=f"Reminder: The task '{task.title}' is due soon!"
            )
            return Response({'message': 'Reminder sent successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Task is not due within the next 24 hours'}, status=status.HTTP_200_OK)
    return Response({'error': 'Task due date is not set'}, status=status.HTTP_400_BAD_REQUEST)



class NotificationDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, *args, **kwargs):
        try:
            notification = Notification.objects.get(pk=pk, user=request.user)  # Ensure the notification belongs to the user
            notification.delete()
            return Response({"message": "Notification deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Notification.DoesNotExist:
            return Response({"error": "Notification not found or you do not have permission."}, status=status.HTTP_404_NOT_FOUND)
