from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)  # Name of the category
    description = models.TextField(blank=True)  # Optional description for the category
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')  # Associate category with the user

    def __str__(self):
        return self.name 