from django.urls import path, include
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path(route='', view=views.home, name="home"),
    path(route='signup/', view=views.signUp, name='signup'),
    path(route='login/', view=views.userLogin, name="login"),
    path(route='profile/', view=views.userProfile, name="profile"),
    path(route='logout/', view=views.userLogout, name="logout"),
    path(route='changepassword/', view=views.userChangePassword, name="changepassword"),
    path(route='myMessages/', view=views.myMessages, name="myMessages"),

    path(route='activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', view=views.activate, name='activate'),
    # path(route='my2/', view=views.myprofile2, name="my2"),

]
