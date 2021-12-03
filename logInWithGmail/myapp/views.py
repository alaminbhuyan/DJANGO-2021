from django.shortcuts import render
from django.contrib.auth import logout


# Create your views here.
def user_logout(request):
    logout(request=request)
    return render(request=request, template_name="social_app/index.html")