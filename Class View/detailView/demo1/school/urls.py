from django.urls import path
from . import views


urlpatterns = [
    path(route='<int:pk>', view=views.StudentDetailView.as_view(), name="studentDetail"),
]
