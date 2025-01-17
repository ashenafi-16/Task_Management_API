# tasks/models.py

from django.db import models
from django.contrib.auth.models import User
from catagories.models import Category  # <-- Import Category model

# Task Model
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')  # Link task to user
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)  # Link task to category (optional)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
