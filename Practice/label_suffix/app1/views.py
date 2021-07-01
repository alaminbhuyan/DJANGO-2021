from django.shortcuts import render
from .models import Mobile, Computer, UserProfile, UserProfile2
from .forms import ComputerForm

# Create your views here.
def home(request):
    mobile_obj = Mobile.objects.all()
    if request.method == "POST":
        form = ComputerForm(request.POST)
        if form.is_valid():
            processor = form.cleaned_data.get('processor')
            motherboard = form.cleaned_data.get('motherboard')
            powersupply = form.cleaned_data.get('powerSupply')
            caseing = form.cleaned_data.get('caseing')
            ram = form.cleaned_data.get('ram')
            price = form.cleaned_data.get('total_price')

            obj = Computer(processor=processor, motherboard=motherboard, powerSupply=powersupply, caseing=caseing,ram=ram, total_price=price)
            obj.save()
            form = ComputerForm()
    else:
        form = ComputerForm()

    com_obj = Computer.objects.all()

    context = {
        'mobiles': mobile_obj,
        'computers': com_obj,
        'form': form
    }
    return render(request=request, template_name="app1/index.html", context= context)


def userProfile(request):
    user_profile = UserProfile2.objects.all()
    # print(request.user.usrename)
    return render(request=request, template_name="app1/home.html",context={'profile': user_profile})
