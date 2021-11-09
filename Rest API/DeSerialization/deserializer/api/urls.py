from django import urls
from django.urls.conf import path
from . import views


urlpatterns = [
    path(route='', view=views.student_create, name="home_page"),
]
