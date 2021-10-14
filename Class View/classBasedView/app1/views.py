from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

# Function based view

def home(request):
    return HttpResponse("<h1>Hi, Alamin this is function based view</h1>")


# Class based view

class HomeView(View):
    def get(self, request):
        return HttpResponse("<h1>Hi, Alamin this is class based view</h1>")


class HomeView2(View):
    name = 'Alamin'
    def get(self, request):
        return HttpResponse(self.name)


class HomeView3(HomeView2):

    def get(self, request):
        return HttpResponse(self.name)