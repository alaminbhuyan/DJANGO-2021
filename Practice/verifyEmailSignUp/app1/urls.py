from django.urls import path
from . import views


urlpatterns = [
    path(route='', view=views.signup, name='signup'),
    path(route='signin/', view=views.signin, name='signin'),
    path(route='account-verify/<str:token>', view=views.account_verify, name='account_verify'),
    path(route='profile/', view=views.profile, name='profile'),
    path(route='logout/', view=views.accountLogout, name='logout'),
]
