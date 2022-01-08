from django.urls import path, include
from . import views



urlpatterns = [
    path(route='', view=views.home, name="home"),
    path(route='signup/', view=views.signUp, name='signup'),
    path(route='login/', view=views.userLogin, name="login"),
    path(route='profile/', view=views.userProfile, name="profile"),
    path(route='logout/', view=views.userLogout, name="logout"),
    path(route='changepassword/', view=views.userChangePassword, name="changepassword"),
    path(route='my/', view=views.myprofile, name="my"),
    # path(route='my2/', view=views.myprofile2, name="my2"),

]


# some user profile password

# 1) username: alamin, password: geekyshows
# 2) username: mim, password: geekyshows