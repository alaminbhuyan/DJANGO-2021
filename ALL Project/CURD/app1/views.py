from django.core import paginator
from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import StudentRegistration
from django.contrib import messages
from django.core.paginator import Paginator





# Create your views here.

#? This function add new record in the database

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg = User(name=name, email=email, password=password)
            reg.save()
            messages.success(request=request, message="You Successfully Add New Record")
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()

    # student_info = User.objects.all() # this is previous line before adding paginator
    student_info = User.objects.all().order_by('id')
    paginator = Paginator(object_list=student_info, per_page=8, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(number=page_number)
    # return render(request, "app1/addAndShow.html", context={'form': fm, 'info':student_info})
    return render(request, "app1/addAndShow.html", context={'form': fm, 'page_obj':page_obj})


#? This function update the database record

def update_data(request, id):
    if request.method == "POST":
        record = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=record)
        if fm.is_valid():
            fm.save()
        messages.success(request=request, message="You Successfully Updated your Record")
        return HttpResponseRedirect('/')
    else:
        record = User.objects.get(pk=id)
        fm = StudentRegistration(instance=record)
    return render(request, "app1/update.html", context={'form':fm})

#? This function delete the record in the database table

def delete_data(request, id):
    if request.method == "POST":
        record = User.objects.get(pk=id)
        record.delete()
        messages.success(request=request, message="You Successfully Delete your Record")
        return HttpResponseRedirect('/')
