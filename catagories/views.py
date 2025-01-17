from rest_framework.permissions import IsAuthenticated  # Ensures only authenticated users can access
from rest_framework.views import APIView  # Base class for API views
from rest_framework.response import Response  # For sending responses in API views
from rest_framework import status  # Contains HTTP status codes
from .models import Category  # Importing the Category model
from .serializers import CategorySerializer  # Importing the Category serializer

# Create a new category
class CategoryCreateView(APIView):
    permission_classes = [IsAuthenticated]  # Only accessible by authenticated users

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Link category to the authenticated user
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return created category data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors

# List all categories for the authenticated user
class CategoryListView(APIView):
    permission_classes = [IsAuthenticated]  # Only accessible by authenticated users

    def get(self, request, *args, **kwargs):
        categories = Category.objects.filter(user=request.user)  # Fetch categories owned by the user
        serializer = CategorySerializer(categories, many=True)  # Serialize multiple categories
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data

# Retrieve a specific category
class CategoryRetrieveView(APIView):
    permission_classes = [IsAuthenticated]  # Only accessible by authenticated users

    def get(self, request, pk, *args, **kwargs):
        try:
            category = Category.objects.get(pk=pk, user=request.user)  # Fetch category by ID for the user
            serializer = CategorySerializer(category)  # Serialize the category
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data
        except Category.DoesNotExist:
            return Response({"error": "Category not found or you do not have permission."}, status=status.HTTP_404_NOT_FOUND)

# Update a specific category by ID
class CategoryUpdateView(APIView):
    permission_classes = [IsAuthenticated]  # Only accessible by authenticated users

    def put(self, request, pk, *args, **kwargs):
        try:
            category = Category.objects.get(pk=pk, user=request.user)  # Fetch category by ID for the user
            serializer = CategorySerializer(category, data=request.data)  # Serialize with new data
            if serializer.is_valid():
                serializer.save()  # Save updated category
                return Response(serializer.data, status=status.HTTP_200_OK)  # Return updated data
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors
        except Category.DoesNotExist:
            return Response({"error": "Category not found or you do not have permission."}, status=status.HTTP_404_NOT_FOUND)

# Delete a specific category
class CategoryDeleteView(APIView):
    permission_classes = [IsAuthenticated]  # Only accessible by authenticated users

    def delete(self, request, pk, *args, **kwargs):
        try:
            category = Category.objects.get(pk=pk, user=request.user)  # Fetch category by ID for the user
            category.delete()  # Delete the category
            return Response({"message": "Category deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({"error": "Category not found or you do not have permission."}, status=status.HTTP_404_NOT_FOUND)
