from django.urls import path
from . import views



urlpatterns = [
    path(route='', view=views.home, name="home"),
    path(route='signup/', view=views.signUp, name='signup'),
    path(route='login/', view=views.userLogin, name="login"),
    path(route='profile/', view=views.userProfile, name="profile"),
    path(route='logout/', view=views.userLogout, name="logout"),
    path(route='changepassword/', view=views.userChangePassword, name="changepassword"),
    path(route='delete/', view=views.deleteConfirmation, name="deleteConfirmation"),
    path(route='delete/<str:email>', view=views.deleteAccount, name="delete"),

]