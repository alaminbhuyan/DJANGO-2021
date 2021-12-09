from django.urls import path, include
from . import views



urlpatterns = [
    path('' , views.Home , name="home"),
    path('login/' , views.Login , name="login"),
    path('register/' , views.Register , name="register"),
    path('forget-password/' , views.ForgetPassword , name="forget_password"),
    path('change-password/<token>/' , views.ChangePassword , name="change_password"),
    path('logout/' , views.Logout , name="logout"),
]
