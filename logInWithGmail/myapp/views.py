from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout




def user_logout(request):
    logout(request=request)
    return HttpResponseRedirect(redirect_to='/')