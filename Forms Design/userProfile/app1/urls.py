from django.urls import path
from . import views


urlpatterns = [
    path(route='', view=views.userLogin, name='login'),
    path(route='home/', view=views.home, name='home'),
    path(route='logout/', view=views.userLogout, name='logout'),
]

# Some user profile password

# 1) username: alamin; password: geekyshows
# 2) username: fatema; password: geekyshows