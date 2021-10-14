from django.urls import path
from . import views

urlpatterns = [
    # path('', views.HomeView.as_view(), name="home_page"),
    path(route='', view=views.HomeView.as_view(), name="home_page"),
    path(route='<int:pk>', view=views.CandidateView.as_view(), name="candidate"),
]
