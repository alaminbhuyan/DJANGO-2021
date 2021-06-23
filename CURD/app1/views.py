from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import StudentRegistration
from django.contrib import messages
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

    student_info = User.objects.all()
    return render(request, "app1/addAndShow.html", context={'form': fm, 'info':student_info})


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
