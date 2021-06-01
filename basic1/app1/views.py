from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("<h3> alamin </h3>")
    dic = {"name":"alamin",
           "age": 21,
           "address":"Dhaka, Uttara, Sector-6"}

    return render(request,"home.html", context = {"dic":dic})


def about(request):
    return HttpResponse("<h1>this is about page</h1>")


def profile(request):
    pass