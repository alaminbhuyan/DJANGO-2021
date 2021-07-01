from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.signUp, name="signup_form"),
    path(route='profile', view=views.user_profile, name="user_profile"),
    path(route='login', view=views.logIn, name="login_form"),
    path(route='logout', view=views.logOut, name="user_logout"),
    path(route='changePassword', view=views.userChangePassword, name="user_changePassword"),
    path(route='changePassword2', view=views.userChangePassword2, name="user_changePassword2"),
    path(route='userdetails/<int:id>', view=views.userDetails, name="user_detail"),
]
