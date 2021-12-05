from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from .forms import LoginForm
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

class HomeTemplateView(TemplateView):
    template_name='myapp/home.html'

@method_decorator(decorator=login_required, name='dispatch')
class DashboardTemplateView(TemplateView):
    template_name='myapp/dashboard.html'



class MyLoginView(LoginView):
    template_name='myapp/login.html'
    authentication_form = LoginForm

@method_decorator(decorator=login_required, name='dispatch')
class MyLogoutView(LogoutView):
    template_name='myapp/logout.html'


@method_decorator(decorator=login_required, name='dispatch')
class MyPasswordChangeView(PasswordChangeView):
    template_name='myapp/changePassword.html'
    success_url='/changepasswordDone/'

@method_decorator(decorator=login_required, name='dispatch')
class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name='myapp/changePasswordDone.html'
