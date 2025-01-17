from django.urls import path
from .views import LoginView, logout_view, PasswordResetView, PasswordResetConfirmView, RegisterView, PasswordChangeView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),  # Route for user registration
    path("api/login/", LoginView.as_view(), name="login"),  # Route for user login
    path("api/logout/", logout_view, name="logout"),  # Route for user logout
    path('api/password_change/', PasswordChangeView.as_view(), name='password_change'),  # Route for password change
    path('api/password_reset/', PasswordResetView.as_view(), name='password_reset'),  # Route for password reset request
    path('api/password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # Route for password reset confirmation
]
