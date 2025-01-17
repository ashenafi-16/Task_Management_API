from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer

# Create a new category
class CategoryCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Associate the category with the authenticated user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List all categories for the authenticated user
class CategoryListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        categories = Category.objects.filter(user=request.user)  # Only the user's categories
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Retrieve a specific category
class CategoryRetrieveView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        try:
            category = Category.objects.get(pk=pk, user=request.user)  # Ensure it belongs to the user
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"error": "Category not found or you do not have permission."}, status=status.HTTP_404_NOT_FOUND)

# Update a specific category by ID
class CategoryUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, *args, **kwargs):
        try:
            category = Category.objects.get(pk=pk, user=request.user)  # Ensure the category belongs to the user
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()  # Save the updated category
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response({"error": "Category not found or you do not have permission."}, status=status.HTTP_404_NOT_FOUND)

# Delete a specific category
class CategoryDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, *args, **kwargs):
        try:
            category = Category.objects.get(pk=pk, user=request.user)  # Ensure it belongs to the user
            category.delete()
            return Response({"message": "Category deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({"error": "Category not found or you do not have permission."}, status=status.HTTP_404_NOT_FOUND)
