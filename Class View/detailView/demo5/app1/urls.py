import imp
from django.urls import path
from .import views

urlpatterns = [
    path(route='<int:pk>/', view=views.HomeDetailView.as_view(), name='home'),
]
