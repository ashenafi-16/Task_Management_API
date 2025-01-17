from rest_framework.permissions import IsAuthenticated  # Importing permission class to restrict views to authenticated users
from rest_framework.views import APIView  # Base class for creating class-based views
from rest_framework.response import Response  # For sending HTTP responses
from rest_framework import status  # Importing HTTP status codes
from .models import Task  # Importing the Task model
from .serializers import TaskSerializer  # Importing the Task serializer for data validation

# Create a new task
class TaskCreateView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can create a task

    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)  # Deserialize incoming data
        if serializer.is_valid():
            serializer.save(user=request.user)  # Save task for the authenticated user
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created task data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if the data is invalid

# List all tasks for the authenticated user
class TaskListView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access their tasks

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(user=request.user)  # Fetch tasks belonging to the authenticated user
        serializer = TaskSerializer(tasks, many=True)  # Serialize all tasks
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return the list of tasks

# Retrieve a specific task
class TaskRetrieveView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can retrieve tasks

    def get(self, request, pk, *args, **kwargs):
        try:
            task = Task.objects.get(pk=pk, user=request.user)  # Ensure the task belongs to the user
            serializer = TaskSerializer(task)  # Serialize the task data
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return the task data
        except Task.DoesNotExist:
            return Response({"error": "Task not found or you do not have permission."}, status=status.HTTP_404_NOT_FOUND)  # Handle task not found

# Update a specific task
class TaskUpdateView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can update tasks

    def put(self, request, pk, *args, **kwargs):
        try:
            task = Task.objects.get(pk=pk, user=request.user)  # Ensure the task belongs to the user
            serializer = TaskSerializer(task, data=request.data)  # Serialize incoming data and bind to the task object
            if serializer.is_valid():
                serializer.save()  # Save the updated task data
                return Response(serializer.data, status=status.HTTP_200_OK)  # Return updated task data
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors if any
        except Task.DoesNotExist:
            return Response({"error": "Task not found or you do not have permission."}, status=status.HTTP_404_NOT_FOUND)  # Handle task not found

# Delete a specific task
class TaskDeleteView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete tasks

    def delete(self, request, pk, *args, **kwargs):
        try:
            task = Task.objects.get(pk=pk, user=request.user)  # Ensure the task belongs to the user
            task.delete()  # Delete the task
            return Response(status=status.HTTP_204_NO_CONTENT)  # Return no content on successful deletion
        except Task.DoesNotExist:
            return Response({"error": "Task not found or you do not have permission."}, status=status.HTTP_404_NOT_FOUND)  # Handle task not found
