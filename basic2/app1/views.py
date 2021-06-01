from django.shortcuts import render
from .forms import MobileForms

# Create your views here.
def home(request):
    if request.method == "POST":
        obj = MobileForms(request.POST)
        if obj.is_valid():
            print("MobileName: ", obj.cleaned_data['mobileName'])
            print("MobileModel: ", obj.cleaned_data['mobileModel'])
            print("MobilePrice: ", obj.cleaned_data['mobilePrice'])
            print("MobilePrice: ", request.POST['mobilePrice'])
            print("Discount offer: ", obj.cleaned_data['offer'])
            obj = MobileForms()
    else:
        obj = MobileForms()
    return render(request, "app1/home.html", context={'form':obj})