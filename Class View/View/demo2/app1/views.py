from re import U
from django.shortcuts import render
from .models import UserSignUp
from django.views import View
from django.http import HttpResponse

# Create your views here.
class HomeView(View):

    def get(self, request):
        return render(request=request, template_name='app1/home.html')
    
    def post(self, request):
        user_name = request.POST.get('username')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print(user_name, first_name, last_name, email, password1, password2)
        user_obj = UserSignUp(username=user_name, firstName=first_name, lastName=last_name, email=email, password1=password1, password2=password2)
        
        user_obj.save()

        return HttpResponse("Form is submitted")