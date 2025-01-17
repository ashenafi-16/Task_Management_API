from django.urls import path
from .views import (
    CategoryCreateView,  # View to create a category
    CategoryListView,    # View to list all categories
    CategoryRetrieveView,  # View to retrieve a specific category
    CategoryUpdateView,  # View to update a category
    CategoryDeleteView   # View to delete a category
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),  # List categories
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),  # Create category
    path('categories/<int:pk>/', CategoryRetrieveView.as_view(), name='category-retrieve'),  # Retrieve category by ID
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),  # Update category by ID
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),  # Delete category by ID
]
