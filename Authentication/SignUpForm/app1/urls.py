from django.urls import path
from . import views


urlpatterns = [
    path(route='', view=views.signUp, name='signup'),
]
