from django.urls import path
from .views import LoginView, logout_view,PasswordResetView, PasswordResetConfirmView,RegisterView,PasswordChangeView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/logout/", logout_view, name="logout"),
    path('api/password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('api/password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('api/password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
