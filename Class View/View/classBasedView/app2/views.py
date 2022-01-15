from django.shortcuts import render
from django.views import View


# Create your views here.

# Rendering html file for function based
def about_home(request):
    context = {"mess":"Hi, this line of sentence is came from context for function based"}
    return render(request=request, template_name="app2/home.html", context=context)


# Rendering html file for class based

class AboutView(View):
    def get(self, request):
        context = {"mess":"Hi, this line of sentence is came from context for class based"}
        return render(request=request, template_name="app2/home.html", context=context)