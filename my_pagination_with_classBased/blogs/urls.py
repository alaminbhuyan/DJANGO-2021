from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home, name="home_page"),
    path(route='', view=views.PostListView.as_view(), name="home_page"),
    path(route='home2/', view=views.PostListView2.as_view(), name="home_page2"),
    path(route='post/<int:pk>', view=views.PostDetailView.as_view(), name="post_page")
]
