from rest_framework import serializers  # Importing DRF serializers
from .models import Category  # Importing the Category model

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # Specify the model to serialize
        fields = ['id', 'name', 'description', 'user']  # Include necessary fields

    def create(self, validated_data):
        # Assign the authenticated user to the category before saving
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)  # Call parent method to create the category
