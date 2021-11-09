from django.urls import path
from . import views


urlpatterns = [
    path(route='', view=views.home, name="home_page"),
    path(route='stuinfo/', view=views.studentInfo2, name="student_info2"),
    path(route='stuinfo/<int:pk>', view=views.studentInfo, name="student_info"),
]