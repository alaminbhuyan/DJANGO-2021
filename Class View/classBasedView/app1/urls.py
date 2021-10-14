from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"), # this for function based
    path('myview/', views.HomeView.as_view(), name="home_class"), # this for class based
    path('myview2/', views.HomeView2.as_view(name="Tania"), name="home_class2"),
    path('myview3/', views.HomeView3.as_view(), name="home_class3"),
]
