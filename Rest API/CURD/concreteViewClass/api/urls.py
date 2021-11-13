from django import urls
from django.urls.conf import path
from . import views


urlpatterns = [
    path(route='', view=views.StudentListCreate.as_view(), name="student_api"),
    path(route='<int:pk>', view=views.StudentRetrieveUpdateDestroy.as_view(), name="student_api2"),
]
