import imp
from django.urls import path
from . import views

urlpatterns = [
    path(route='register/', view=views.UserRegistrationView.as_view(), name='register'),
    path(route='login/', view=views.UserLoginView.as_view(), name='login'),
    path(route='profile/', view=views.UserProfileView.as_view(), name='profile'),
    path(route='changepassword/', view=views.UserChangePasswordView.as_view(), name='changepassword'),
    path(route='send-reset-password-email/', view=views.SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path(route='reset-password/<uid>/<token>/', view=views.UserPasswordResetView.as_view(), name='resetPassword'),
]
