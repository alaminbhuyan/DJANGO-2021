from django.db import models

# Create your models here.


class RegistrationForm(models.Model):
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    fatherName = models.CharField(max_length=150)
    motherName = models.CharField(max_length=150)
    admissionSession = models.CharField(max_length=150)
    studentID = models.CharField(max_length=150)
    semester = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    mobileNumber = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    gender = models.CharField(max_length=50)
    payment = models.CharField(max_length=100)
    formSubmited = models.DateField(auto_now_add=True)
