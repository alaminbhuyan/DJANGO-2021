from django.urls import path
from . import views


urlpatterns = [
    path('', views.about_home, name="about_home"), # this for function based
    path('aboutview/', views.AboutView.as_view(), name="aboutview"),
]
