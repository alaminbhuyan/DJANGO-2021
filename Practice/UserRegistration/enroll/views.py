from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from .forms import SignUpForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

# first looked like that
# def signUp(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request=request, message="Your account Created Successfully")
#     else:
#         form = UserCreationForm()

#     # this is context part
#     context = {
#         'form':form,
#     }
#     return render(request=request, template_name="enroll/signup.html", context=context)

def signUp(request):
    if request.method == "POST":
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request=request, message="Your account Created Successfully")
            messages.success(request=request, message="Please LogIn your Account")
            return HttpResponseRedirect("/login")
    else:
        form = SignUpForm()

    # this is context part
    context = {
        'form':form,
    }
    return render(request=request, template_name="enroll/signup.html", context=context)


def logIn(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                # user_name = form.cleaned_data['username'] # we can use this way also
                user_name = form.cleaned_data.get('username')
                user_password = form.cleaned_data.get('password')
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    # login(request,user)
                    login(request=request,user=user)
                    messages.success(request=request, message="Logged In successfully")
                    return HttpResponseRedirect('/profile')
        else:
            form = AuthenticationForm()

        # this is context part
        context = {
            'form':form,
        }
        return render(request=request, template_name="enroll/login.html", context=context)
    else:
        return HttpResponseRedirect('/profile')

# This is for to do redirect 
# first condition

# def user_profile(request):
#     return render(request=request, template_name="enroll/profile.html", context={'user':request.user})

# after first edit

# def user_profile(request):
#     if request.user.is_authenticated:
#         return render(request=request, template_name="enroll/profile.html", context={'user':request.user})
#     else:
#         return HttpResponseRedirect('/login')

# after first edit
# def user_profile(request):
#     if request.user.is_authenticated:
#         form = UserChangeForm(instance=request.user)

#         # this is context
#         context = {
#             'form':form,
#             'user':request.user
#         }
#         return render(request=request, template_name="enroll/profile.html", context=context)
#     else:
#         return HttpResponseRedirect('/login')

# after second edit
# def user_profile(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             form = EditUserProfileForm(data=request.POST, instance=request.user)
#             if form.is_valid():
#                 messages.success(request=request, message="Your profile Updated Successfully")
#                 form.save()
#         else:
#             form = EditUserProfileForm(instance=request.user)

#         # this is context
#         context = {
#             'form':form,
#             'user':request.user
#         }
#         return render(request=request, template_name="enroll/profile.html", context=context)
#     else:
#         return HttpResponseRedirect('/login')

# after third edit
# def user_profile(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             if request.user.is_superuser == True:
#                 form = EditAdminProfileForm(data=request.POST, instance=request.user)
#             else:
#                 form = EditUserProfileForm(data=request.POST, instance=request.user)
#             if form.is_valid():
#                 messages.success(request=request, message="Your profile Updated Successfully")
#                 form.save()
#         else:
#             if request.user.is_superuser == True:
#                 form = EditAdminProfileForm(instance=request.user)
#             else:
#                 form = EditUserProfileForm(instance=request.user)

#         # this is context
#         context = {
#             'form':form,
#             'user':request.user
#         }
#         return render(request=request, template_name="enroll/profile.html", context=context)
#     else:
#         return HttpResponseRedirect('/login')



def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                form = EditAdminProfileForm(data=request.POST, instance=request.user)
                all_user = User.objects.all()
            else:
                form = EditUserProfileForm(data=request.POST, instance=request.user)
            if form.is_valid():
                all_user = None
                messages.success(request=request, message="Your profile Updated Successfully")
                form.save()
        else:
            if request.user.is_superuser == True:
                form = EditAdminProfileForm(instance=request.user)
                all_user = User.objects.all()
            else:
                form = EditUserProfileForm(instance=request.user)
                all_user = None

        # this is context
        context = {
            'form': form,
            'user': request.user,
            'all_user': all_user
        }
        return render(request=request, template_name="enroll/profile.html", context=context)
    else:
        return HttpResponseRedirect('/login')






def logOut(request):
    logout(request=request)
    return HttpResponseRedirect('/login')

# Change password with old password
def userChangePassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request=request, user=form.user) # for keep login
                messages.success(request=request, message="You successfully Changed your Password")
                return HttpResponseRedirect('/profile')
        else:
            form = PasswordChangeForm(user=request.user)

        # this is context part
        context = {
                'form':form,
            }
        return render(request=request, template_name="enroll/changePassword.html", context=context)
    else:
        return HttpResponseRedirect('/login')

# Change password without old password
def userChangePassword2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request=request, user=form.user) # for keep login
                messages.success(request=request, message="You successfully Changed your Password")
                return HttpResponseRedirect('/profile')
        else:
            form = SetPasswordForm(user=request.user)

        # this is context part
        context = {
                'form':form,
            }
        return render(request=request, template_name="enroll/changePassword2.html", context=context)
    else:
        return HttpResponseRedirect('/login')


# User details form function
def userDetails(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        form = EditAdminProfileForm(instance=pi)
        # this is all context
        context = {
            "form" : form,
            'user': request.user,
        }
        return render(request=request, template_name="enroll/userdetail.html", context=context)
    else:
        return HttpResponseRedirect('/login')