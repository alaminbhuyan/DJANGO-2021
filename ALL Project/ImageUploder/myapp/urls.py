from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.home, name="home_page"),
    path(route='delete/<int:id>', view=views.delete_data, name="delete_data"),
]
