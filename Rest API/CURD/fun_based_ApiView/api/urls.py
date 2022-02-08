from django import urls
from django.urls.conf import path
from . import views


urlpatterns = [
    path(route='', view=views.StudentAPI, name="student_api"),
    path(route='<int:pk>', view=views.StudentAPI, name="student_api"),
]
