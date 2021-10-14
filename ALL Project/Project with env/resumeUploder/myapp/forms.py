from django import forms
from django.forms import fields
from .models import Resume


GENDER_CHOICES = [
 ('Male', 'Male'),
 ('Female', 'Female')
]

JOB_CITY_CHOICE = [
 ('Dhaka', 'Dhaka'),
 ('Comilla', 'Comilla'),
 ('Sylhet', 'Sylhet'),
 ('Chittagong', 'Chittagong'),
 ('Gazipur', 'Gazipur'),
 ('Chadpur', 'Chadpur')
]


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple, label="Preferred Job Locations")
    class Meta:
        model = Resume
        fields = ['name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_files']

        labels = {'name':'Full Name', 'dob': 'Date of Birth', 'pin':'Pin Code', 'mobile':'Mobile No.', 'email':'Email ID','profile_image':'Profile Image', 'my_files':'Document'}

        widgets = {
            'name' :forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }