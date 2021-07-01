from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.home, name="home_page"),
    path(route='user', view=views.userProfile, name="user_profile"),
]
