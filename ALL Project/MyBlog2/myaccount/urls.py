from django.urls import path 
from . import views



urlpatterns = [
    path(route='signup/', view=views.signup, name='signup'),
    path(route='signin/', view=views.signin, name='signin'),
    path(route='account-verify/<slug:token>', view=views.account_verify, name='account_verify'),
    path(route='profile/', view=views.profile, name='profile'),
    path(route='logout/', view=views.accountLogout, name='logout'),
    path(route='changepassword/', view=views.userChangePassword, name="changepassword"),
    path(route='delete/', view=views.deleteConfirmation, name="deleteConfirmation"),
    path(route='delete/<str:email>', view=views.deleteAccount, name="delete"),
]