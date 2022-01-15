from django.urls import path 
from . import views

urlpatterns = [
    path(route='', view=views.HomeListView.as_view(), name='home'),
]
