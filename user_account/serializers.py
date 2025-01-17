from django.contrib.auth import authenticate  # Import authenticate method for user login
from rest_framework import serializers  # Import serializers to handle data validation and serialization
from django.contrib.auth.models import User  # Import the built-in User model
from django.contrib.auth.password_validation import validate_password  # Import password validation utility
from django.contrib.auth import get_user_model  # Get the custom user model

# Registration serializer to handle user registration
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)  # Password field (write-only)
    password_confirm = serializers.CharField(write_only=True, required=True)  # Confirm password field (write-only)

    class Meta:
        model = User  # Use the built-in User model
        fields = ['username', 'password', 'password_confirm', 'email']  # Fields for registration

    def validate(self, data):
        # Ensure password and password_confirm match
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        # Remove password_confirm field, not needed anymore
        validated_data.pop('password_confirm', None)
        user = User.objects.create_user(
            username=validated_data['username'],  # Create user with the provided data
            email=validated_data.get('email', ''),  # Get email or empty string if not provided
            password=validated_data['password']  # Set the user's password
        )
        return user


# Login serializer to authenticate users based on username and password
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # Username field
    password = serializers.CharField(write_only=True)  # Password field (write-only)

    def validate(self, data):
        username = data.get("username")  # Get username from the request data
        password = data.get("password")  # Get password from the request data

        if username and password:
            user = authenticate(username=username, password=password)  # Attempt user authentication
            if user:
                if not user.is_active:  # Check if user is active
                    raise serializers.ValidationError("User is not active.")
                data["user"] = user  # Add authenticated user to data
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")  # Ensure both fields are provided
        return data


# Password change serializer to handle password updates for authenticated users
class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)  # Old password (write-only)
    new_password = serializers.CharField(write_only=True)  # New password (write-only)
    confirm_password = serializers.CharField(write_only=True)  # Confirm new password (write-only)

    def validate(self, attrs):
        old_password = attrs.get('old_password')  # Get old password
        new_password = attrs.get('new_password')  # Get new password
        confirm_password = attrs.get('confirm_password')  # Get confirm password

        user = self.context['request'].user  # Get the authenticated user

        # Check if the old password is correct
        if not user.check_password(old_password):
            raise serializers.ValidationError("Old password is incorrect")

        # Check if the new password and confirm password match
        if new_password != confirm_password:
            raise serializers.ValidationError("New password and confirmation do not match")

        return attrs

    def save(self):
        user = self.context['request'].user  # Get the authenticated user
        new_password = self.validated_data['new_password']  # Get the new password
        user.set_password(new_password)  # Set the new password
        user.save()  # Save the user with the updated password

# Serializer to handle password reset request
class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()  # Email field for password reset request

    def validate_email(self, value):
        # Check if the email exists in the system
        user_model = get_user_model()  # Get the custom user model
        if not user_model.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")  # Raise error if no user exists with this email
        return value


# Serializer to handle password reset confirmation
class PasswordResetConfirmSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()  # Encoded user ID
    token = serializers.CharField()  # Token for password reset confirmation
    new_password = serializers.CharField(write_only=True)  # New password field (write-only)

    def validate(self, data):
        # Additional validation can be added if needed
        return data
