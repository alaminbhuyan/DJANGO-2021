from django.urls import path
from . import views



urlpatterns = [
    path(route='', view=views.home, name="home"),
    path(route='signup/', view=views.signUp, name='signup'),
    path(route='login/', view=views.userLogin, name="login"),
    path(route='profile/', view=views.userProfile, name="profile"),
    path(route='logout/', view=views.userLogout, name="logout"),
    path(route='changepassword/', view=views.userChangePassword, name="changepassword"),
    path(route='my/', view=views.myprofile, name="my"),

]