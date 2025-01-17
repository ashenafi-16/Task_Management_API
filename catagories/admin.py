from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'description')  # Show these fields in the admin panel
    search_fields = ('name', 'user')  # Enable search by name and user
