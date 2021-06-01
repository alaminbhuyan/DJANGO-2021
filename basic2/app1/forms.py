from django import forms

class MobileForms(forms.Form):
    mobileName = forms.CharField(label="Mobile Name", label_suffix=" ")
    mobileModel = forms.CharField(max_length=10,label="Mobile Model", label_suffix=' ')
    mobilePrice = forms.IntegerField(label="Mobile Price", label_suffix=' ')
    offer =       forms.BooleanField(label="Discount offer ",required=False)