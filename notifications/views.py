from rest_framework.decorators import api_view  # Importing the api_view decorator to define view functions
from rest_framework.response import Response  # For sending HTTP responses
from rest_framework import status  # Importing HTTP status codes
from django.utils import timezone  # Importing timezone for working with date and time
from tasks.models import Task  # Importing the Task model
from .models import Notification  # Importing the Notification model
from rest_framework.permissions import IsAuthenticated  # To restrict access to authenticated users
from rest_framework.views import APIView  # Base class for class-based views

# View function to send a task reminder
@api_view(['POST'])
def send_task_reminder(request, task_id):
    try:
        task = Task.objects.get(id=task_id)  # Retrieve the task by ID
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)  # Task not found

    if task.due_date:
        time_remaining = task.due_date - timezone.now()  # Calculate time remaining until task due date
        if time_remaining.total_seconds() <= 86400:  # Check if task is due within 24 hours
            Notification.objects.create(  # Create a reminder notification for the user
                user=task.user,
                task=task,
                message=f"Reminder: The task '{task.title}' is due soon!"
            )
            return Response({'message': 'Reminder sent successfully'}, status=status.HTTP_200_OK)  # Success response
        else:
            return Response({'message': 'Task is not due within the next 24 hours'}, status=status.HTTP_200_OK)  # Task not due yet
    return Response({'error': 'Task due date is not set'}, status=status.HTTP_400_BAD_REQUEST)  # No due date set for the task


# Class-based view to delete a notification
class NotificationDeleteView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can delete notifications

    def delete(self, request, pk, *args, **kwargs):
        try:
            notification = Notification.objects.get(pk=pk, user=request.user)  # Ensure the notification belongs to the authenticated user
            notification.delete()  # Delete the notification
            return Response({"message": "Notification deleted successfully."}, status=status.HTTP_204_NO_CONTENT)  # Success response
        except Notification.DoesNotExist:
            return Response({"error": "Notification not found or you do not have permission."}, status=status.HTTP_404_NOT_FOUND)  # Notification not found or user not authorized
