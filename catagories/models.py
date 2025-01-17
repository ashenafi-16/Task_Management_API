from django.db import models  # Importing Django's models module
from django.contrib.auth.models import User  # Importing the User model to associate categories with users

class Category(models.Model):
    name = models.CharField(max_length=255)  # Name of the category (required field)
    description = models.TextField(blank=True)  # Optional description for the category
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')  # Link category to a user

    def __str__(self):
        return self.name  # Return the category name when the category object is printed
