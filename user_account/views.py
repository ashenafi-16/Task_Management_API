from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


# Import serializers
from .serializers import (
    LoginSerializer,
    PasswordResetSerializer,
    PasswordResetConfirmSerializer,
    RegistrationSerializer,
    PasswordChangeSerializer
)


# Registration view: Allows users to register by providing username, email, and password
class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
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
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "message": "Login successful!"})


# Logout view: Logs the user out by deleting the auth token
@api_view(["POST"])
def logout_view(request):
    request.user.auth_token.delete()
    return Response({"message": "Logged out successfully!"})


# Password change view: Allows authenticated users to change their password
class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PasswordChangeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()  # This saves the new password
            return Response({"message": "Password changed successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetView(APIView):
    serializer_class = PasswordResetSerializer
    permission_classes = [AllowAny]  # Allow unauthenticated users
    
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                # Fetch the user by email
                user = get_user_model().objects.get(email=email)
            except get_user_model().DoesNotExist:
                return Response({"detail": "User with this email does not exist."}, status=status.HTTP_400_BAD_REQUEST)

            # Generate token and UID
            uid = urlsafe_base64_encode(str(user.pk).encode())
            token = default_token_generator.make_token(user)
            
            # Construct the reset URL
            reset_url = f"{settings.FRONTEND_RESET_URL.format(uid=uid, token=token)}"
            
            # Send reset email
            subject = "Password Reset Request"
            message = f"Click the link to reset your password: {reset_url}"
            send_mail(subject, message, 'no-reply@yourdomain.com', [email])
            
            return Response({"detail": "Password reset link sent to email"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View to handle password reset confirmation
class PasswordResetConfirmView(APIView):
    serializer_class=PasswordResetConfirmSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Decode the UID and validate the token
                uidb64 = serializer.validated_data['uidb64']
                token = serializer.validated_data['token']
                uid = urlsafe_base64_decode(uidb64).decode()
                user = get_user_model().objects.get(pk=uid)
                
                # Check if the token is valid
                if not default_token_generator.check_token(user, token):
                    return Response({"detail": "Invalid token or token expired."}, status=status.HTTP_400_BAD_REQUEST)
                
                # Reset the password
                user.set_password(serializer.validated_data['new_password'])
                user.save()
                return Response({"detail": "Password has been reset successfully."}, status=status.HTTP_200_OK)
            
            except (get_user_model().DoesNotExist, ValueError):
                return Response({"detail": "Invalid UID or user does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)