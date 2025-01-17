from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'user']  # Include necessary fields

    def create(self, validated_data):
        # Ensure the category is created for the authenticated user
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
