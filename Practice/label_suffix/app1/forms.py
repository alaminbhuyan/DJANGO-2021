from django import forms
from .models import Computer, Mobile


class ComputerForm(forms.ModelForm):
    # processor = forms.CharField(label_suffix='')
    class Meta:
        model = Computer
        fields = ['processor','motherboard','powerSupply','caseing','ram','total_price']
