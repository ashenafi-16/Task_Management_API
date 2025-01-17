from django.urls import path
from .views import (
    TaskCreateView, TaskListView, TaskRetrieveView, TaskUpdateView, TaskDeleteView
)

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),          # List all tasks
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),  # Create a task
    path('tasks/<int:pk>/', TaskRetrieveView.as_view(), name='task-retrieve'),  # Retrieve a task
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),  # Update a task
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),  # Delete a task
]
