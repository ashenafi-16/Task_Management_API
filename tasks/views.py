from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

# Create a new task
class TaskCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Save task for the authenticated user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List all tasks for the authenticated user
class TaskListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(user=request.user)  # Only return tasks for the logged-in user
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Retrieve a specific task
class TaskRetrieveView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        try:
            task = Task.objects.get(pk=pk, user=request.user)  # Ensure the task belongs to the user
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error": "Task not found or you do not have permission."}, status=status.HTTP_404_NOT_FOUND)

# Update a specific task
class TaskUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, *args, **kwargs):
        try:
            task = Task.objects.get(pk=pk, user=request.user)  # Ensure the task belongs to the user
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({"error": "Task not found or you do not have permission."}, status=status.HTTP_404_NOT_FOUND)

# Delete a specific task
class TaskDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, *args, **kwargs):
        try:
            task = Task.objects.get(pk=pk, user=request.user)  # Ensure the task belongs to the user
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  # No need for a message
        except Task.DoesNotExist:
            return Response({"error": "Task not found or you do not have permission."}, status=status.HTTP_404_NOT_FOUND)