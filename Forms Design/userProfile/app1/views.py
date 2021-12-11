from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import EveryUserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    # user = EveryUserProfile.objects.get(id=pk)
    # print(user)
    return render(request=request, template_name='app1/home.html')

# def sample_view(request):
#     current_user = request.user
#     user_obj = EveryUserProfile.objects.get(id=current_user.id)
#     # x = current_user.id
#     print(user_obj)
#     return render(request=request, template_name="app1/home.html", context={'user_obj' : user_obj})


# Login form function
def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_password = form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                # print(user.id)
                # obj = EveryUserProfile.objects.get(id=user.pk)
                # print(obj.username)
                if user is not None:
                    login(request=request, user=user)
                    # print(request.user.id)
                    messages.success(request=request, message="LogIn successfully!!")
                    return HttpResponseRedirect(redirect_to='/home/')
        else:
            form = AuthenticationForm()
        # obj = EveryUserProfile.objects.all()
        # print(obj)
        return render(request=request, template_name="app1/userLogin.html", context={'form' : form})
    else:
        # return HttpResponseRedirect(redirect_to='/')
        return HttpResponse("You are already login")

# Logout form function
def userLogout(request):
    logout(request=request)
    messages.success(request=request, message="Logout successfully!!")
    return HttpResponseRedirect(redirect_to='/')
