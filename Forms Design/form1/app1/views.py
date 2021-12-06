from django.shortcuts import render
from .forms import UserForm



# Create your views here.
def home(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            print("form validated")
            print("UserName: ", form.cleaned_data['username'])
    else:
        form = UserForm()
    return render(request=request, template_name='app1/home.html', context={'form' : form})