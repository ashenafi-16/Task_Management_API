from rest_framework.views import APIView  # To create class-based views that handle HTTP requests
from rest_framework.response import Response  # For returning HTTP responses
from rest_framework.permissions import AllowAny, IsAuthenticated  # Permissions for access control
from rest_framework.decorators import api_view  # For defining function-based views
from rest_framework import status  # For handling HTTP status codes like 200 OK, 400 Bad Request
from django.core.mail import send_mail  # For sending emails, used in password reset functionality
from django.contrib.auth.tokens import default_token_generator  # To generate and validate tokens for password reset
from django.contrib.auth.models import User  # Default User model for user authentication
from django.conf import settings  # For accessing project settings like frontend URLs
from rest_framework.authtoken.models import Token  # For token-based authentication management
from django.contrib.auth import get_user_model  # For accessing the user model, especially for custom user models
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  # For encoding/decoding user ID in URLs

# Import serializers used to validate and transform data
from .serializers import (
    LoginSerializer,  # Handles validation of user login credentials
    PasswordResetSerializer,  # Handles validation for initiating password reset
    PasswordResetConfirmSerializer,  # Handles validation for resetting the password
    RegistrationSerializer,  # Handles user registration data validation
    PasswordChangeSerializer  # Handles password change validation for authenticated users
)


# Registration view: Allows users to register by providing username, email, and password
class RegisterView(APIView):
    def post(self, request):
        # Validate the data using the RegistrationSerializer
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Create and save the user
            return Response({
                "message": "User registered successfully!",
                "user": {
                    "username": user.username,
                    "email": user.email
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login view: Allows users to log in and get an authentication token
class LoginView(APIView):
    permission_classes = [AllowAny]  # Allow unauthenticated users to log in

    def post(self, request):
        # Validate the login credentials using the LoginSerializer
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Raise validation error if credentials are invalid
        user = serializer.validated_data["user"]
        
        # Generate or retrieve the auth token for the user
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "message": "Login successful!"})


# Logout view: Logs the user out by deleting the auth token
@api_view(["POST"])  # Function-based view to log out the user
def logout_view(request):
    request.user.auth_token.delete()  # Delete the authentication token to log the user out
    return Response({"message": "Logged out successfully!"})


# Password change view: Allows authenticated users to change their password
class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can change their password

    def post(self, request):
        # Validate and change the user's password using PasswordChangeSerializer
        serializer = PasswordChangeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()  # Save the new password to the user
            return Response({"message": "Password changed successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Password reset view: Allows users to request a password reset by providing their email
class PasswordResetView(APIView):
    serializer_class = PasswordResetSerializer
    permission_classes = [AllowAny]  # Allow unauthenticated users to request a password reset
    
    def post(self, request):
        # Validate the email using PasswordResetSerializer
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                # Fetch the user by their email address
                user = get_user_model().objects.get(email=email)
            except get_user_model().DoesNotExist:
                return Response({"detail": "User with this email does not exist."}, status=status.HTTP_400_BAD_REQUEST)

            # Generate token and UID for password reset
            uid = urlsafe_base64_encode(str(user.pk).encode())  # Encode user ID
            token = default_token_generator.make_token(user)  # Generate password reset token
            
            # Construct the password reset URL
            reset_url = f"{settings.FRONTEND_RESET_URL.format(uid=uid, token=token)}"
            
            # Send the reset URL to the user's email
            subject = "Password Reset Request"
            message = f"Click the link to reset your password: {reset_url}"
            send_mail(subject, message, 'no-reply@yourdomain.com', [email])
            
            return Response({"detail": "Password reset link sent to email"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View to handle password reset confirmation: Allows users to reset their password using the reset token and UID
class PasswordResetConfirmView(APIView):
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = [AllowAny]  # Allow unauthenticated users to reset their password

    def post(self, request):
        # Validate the reset data using PasswordResetConfirmSerializer
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Decode the UID and validate the token
                uidb64 = serializer.validated_data['uidb64']
                token = serializer.validated_data['token']
                uid = urlsafe_base64_decode(uidb64).decode()  # Decode the user ID
                user = get_user_model().objects.get(pk=uid)
                
                # Validate the token
                if not default_token_generator.check_token(user, token):
                    return Response({"detail": "Invalid token or token expired."}, status=status.HTTP_400_BAD_REQUEST)
                
                # Reset the password
                user.set_password(serializer.validated_data['new_password'])
                user.save()
                return Response({"detail": "Password has been reset successfully."}, status=status.HTTP_200_OK)
            
            except (get_user_model().DoesNotExist, ValueError):
                return Response({"detail": "Invalid UID or user does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
