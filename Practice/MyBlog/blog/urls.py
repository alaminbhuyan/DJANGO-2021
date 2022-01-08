from django.urls import path
from . import views


urlpatterns = [
    path(route='', view=views.post, name='post'),
    path(route='articles/', view=views.articles, name='articles'),
]
