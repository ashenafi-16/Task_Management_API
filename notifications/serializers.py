from rest_framework import serializers  # Importing DRF serializers to handle serialization
from .models import Notification  # Importing the Notification model

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification  # Specify the model to serialize
        fields = '__all__'  # Include all fields from the Notification model in the serialization
