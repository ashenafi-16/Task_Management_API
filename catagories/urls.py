from django.urls import path
from .views import (
    CategoryCreateView,
    CategoryListView,
    CategoryRetrieveView,
    CategoryUpdateView,
    CategoryDeleteView
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),  # List categories
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),  # Create category
    path('categories/<int:pk>/', CategoryRetrieveView.as_view(), name='category-retrieve'),  # Retrieve category by ID
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),  # Update category by ID
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),  # Delete category by ID
]
