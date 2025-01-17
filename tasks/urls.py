from django.urls import path  # Importing path to define URL routes
from .views import (
    TaskCreateView, TaskListView, TaskRetrieveView, TaskUpdateView, TaskDeleteView  # Importing views for task operations
)

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),          # URL to list all tasks
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),  # URL to create a new task
    path('tasks/<int:pk>/', TaskRetrieveView.as_view(), name='task-retrieve'),  # URL to retrieve a task by ID
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),  # URL to update a task by ID
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),  # URL to delete a task by ID
]
