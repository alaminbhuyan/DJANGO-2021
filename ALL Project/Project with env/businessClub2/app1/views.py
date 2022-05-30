from django.shortcuts import render, HttpResponseRedirect
from .models import RegistrationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home(request):

    return render(request=request, template_name='app1/index.html')

# @csrf_exempt
def registrationform(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        fathername = request.POST['fathername']
        mothername = request.POST['mothername']
        admission = request.POST['admission']
        studentId = request.POST['stuid']
        semester = request.POST['semester']
        email = request.POST['email']
        mobilenumber = request.POST['mobilenumber']
        address = request.POST['address']
        gender = request.POST['gender']
        payment = request.POST['paymentMethod']

        user = RegistrationForm(firstName=fname, lastName=lname, fatherName=fathername, motherName=mothername,
                                admissionSession=admission, studentID=studentId, semester=semester, email=email, mobileNumber=mobilenumber, address=address, gender=gender, payment=payment)

        user.save()
        messages.success(request=request, message="Forms submitted")
        return HttpResponseRedirect(redirect_to='/')
    return render(request=request, template_name='app1/userForms.html')


def about(request):
    return render(request=request, template_name='app1/about.html')

def contact(request):
    return render(request=request, template_name='app1/contact.html')
