from django.urls import path
from . import views


urlpatterns = [
    path(route='', view=views.StudentListView.as_view(), name="studentList"),
    path(route='<int:pk>', view=views.StudentDetailView.as_view(), name="studentDetail"),
]
