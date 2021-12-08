from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, EditUserProfileForm, MyAuthenticationForm, MyPasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# new import for user verification using gmail

from django.http import HttpResponse
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib import messages





# Signup form function
def signUp(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                check_email = form.cleaned_data['email']
                user_obj = User.objects.filter(email=check_email).first()
                if user_obj:
                    messages.error(request=request, message="This Email already Taken. Try with different valid Email....!")
                    return HttpResponseRedirect(redirect_to='/signup/')
                # save form in the memory not in database
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                # to get he domain of the current site
                current_site = get_current_site(request=request)
                mail_subject = "Activation link has been sent to your email Id"
                mailMessage = render_to_string(template_name='app1/acc_active_email.html',context={
                'user' : user,
                'domain' : current_site.domain,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : account_activation_token.make_token(user)})
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(mail_subject, mailMessage, to=[to_email])
                email.send()
                return HttpResponseRedirect(redirect_to='/myMessages/')
                # form.save()
        else:
            form = SignUpForm()
        return render(request=request, template_name='app1/signup.html', context={'form' : form})
    else:
        return HttpResponseRedirect(redirect_to='/profile/')

# Login form function
def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = MyAuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_password = form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    login(request=request, user=user)
                    messages.success(request=request, message="LogIn successfully!!")
                    return HttpResponseRedirect(redirect_to='/profile/')
        else:
            form = MyAuthenticationForm()
        return render(request=request, template_name="app1/userLogin.html", context={'form' : form})
    else:
        return HttpResponseRedirect(redirect_to='/profile/')

# Profile page function
def userProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditUserProfileForm(data = request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request=request, message="Profile Updated")
                form.save()
        else:
            form = EditUserProfileForm(instance=request.user)
        return render(request=request, template_name="app1/profile.html", context={'name' : request.user, 'form': form})
    else:
        return HttpResponseRedirect(redirect_to='/login/')


# User change Password with old password
def userChangePassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MyPasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request=request, message="Password updated Successfully!!")
                update_session_auth_hash(request=request, user=form.user)
                return HttpResponseRedirect(redirect_to='/profile/')
        else:
            form = MyPasswordChangeForm(user=request.user)
        return render(request=request, template_name="app1/changepassword.html", context={'form' : form})
    else:
        return HttpResponseRedirect(redirect_to='/login/')



# Logout form function
def userLogout(request):
    logout(request=request)
    messages.success(request=request, message="LogOut Successfully!!")
    return HttpResponseRedirect(redirect_to='/')

# Message function
def myMessages(request):
    return render(request=request, template_name="app1/messages.html")


# Home function
def home(request):
    return render(request=request, template_name="app1/home.html")


# comment: Activation function
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        messages.success(request=request, message="Thank you for your email confirmation. Now you can login your account")
        user.save()
        return HttpResponseRedirect(redirect_to='/login/')
        # return HttpResponse("Thank you for your email confirmation. Now you can login your account")
    else:
        # messages.success(request=request, message="Activation link is invalid")
        return HttpResponse("<h1 style='color:blue;'>A Blue Heading</h1>")