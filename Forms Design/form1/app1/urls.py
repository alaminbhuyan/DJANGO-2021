from django.urls import path
from . import views


urlpatterns = [
    path(route='', view=views.home, name='home'),
    path(route='next', view=views.home2, name='home2'),
]
