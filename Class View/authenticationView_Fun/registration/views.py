from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@login_required
def profile(request):
    return render(request=request, template_name="registration/profile.html")


@login_required
def about(request):
    return render(request=request, template_name="registration/about.html")

@staff_member_required
def confidential(request):
    return render(request=request, template_name="registration/confidential.html")