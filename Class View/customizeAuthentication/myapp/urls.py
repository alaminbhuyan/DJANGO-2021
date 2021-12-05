from django.urls import path, include
from . import views as myauth_views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from .forms import LoginForm


urlpatterns = [
    # path(route='accounts/', view=include('django.contrib.auth.urls')),

#     path(route='', view=TemplateView.as_view(template_name='myapp/home.html'), name='home'),

#     path(route='dashboard/', view=TemplateView.as_view(template_name='myapp/dashboard.html'), name='dashboard'),

#     path('login/', view=auth_views.LoginView.as_view(template_name='myapp/login.html', authentication_form=LoginForm), name='login'),

#     path('logout/', view=auth_views.LogoutView.as_view(template_name='myapp/logout.html'), name='logout'),

#     path('changepassword/', view=auth_views.PasswordChangeView.as_view(template_name='myapp/changePassword.html', success_url='/changepasswordDone/'), name='changepassword'),

#     path('changepasswordDone/', view=auth_views.PasswordChangeDoneView.as_view(template_name='myapp/changePasswordDone.html'), name='changepasswordDone'),
# # =========================================================================================================
#     # path('resetpassword/', view=auth_views.PasswordResetView.as_view(template_name='myapp/resetPassword.html', success_url='/resetpasswordDone/'), name='resetpassword'),

#     # path('resetpasswordDone/', view=auth_views.PasswordResetDoneView.as_view(template_name='myapp/resetPasswordDone.html'), name='resetpasswordDone'),

#     # path('resetpasswordConfirm/', view=auth_views.PasswordResetConfirmView.as_view(template_name='myapp/resetpasswordConfirm.html', success_url='/resetDone/'), name='resetpasswordConfirm'),

#     # path('resetDone/', view=auth_views.PasswordResetConfirmView.as_view(template_name='myapp/resetDone.html'), name='resetDone'),

# ===========================================================================================================

    path(route='', view=myauth_views.HomeTemplateView.as_view(), name='home'),

    path(route='dashboard/', view=myauth_views.DashboardTemplateView.as_view(), name='dashboard'),

    path('login/', view=myauth_views.MyLoginView.as_view(), name='login'),

    path('logout/', view=myauth_views.MyLogoutView.as_view(), name='logout'),

    path('changepassword/', view=myauth_views.MyPasswordChangeView.as_view(), name='changepassword'),

    path('changepasswordDone/', view=myauth_views.MyPasswordChangeDoneView.as_view(), name='changepasswordDone'),
]
