from django import urls
from django.urls.conf import path
from . import views


urlpatterns = [
    path(route='', view=views.StudentAPI.as_view(), name="student_api")
]
