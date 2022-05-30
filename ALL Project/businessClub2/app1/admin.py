from django.contrib import admin
from .models import RegistrationForm

# Register your models here.


@admin.register(RegistrationForm)
class RegistrationFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstName', 'lastName', 'fatherName', 'motherName', 'admissionSession',
                    'studentID', 'semester', 'email', 'mobileNumber', 'address', 'gender', 'payment', 'formSubmited']
