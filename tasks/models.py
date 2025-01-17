from django.db import models  # Importing Django's models module
from django.contrib.auth.models import User  # Importing the User model to link tasks with users
from catagories.models import Category  # Importing the Category model to associate tasks with categories

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')  # Link task to a user (one-to-many relationship)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)  # Link task to a category (optional)
    title = models.CharField(max_length=255)  # Title of the task
    description = models.TextField(blank=True, null=True)  # Optional description of the task
    completed = models.BooleanField(default=False)  # Flag to mark if the task is completed
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set the update timestamp

    def __str__(self):
        return self.title  # Return the task title when the task object is printed
