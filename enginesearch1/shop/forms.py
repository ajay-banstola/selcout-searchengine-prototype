from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import validate_email

class products_form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Which part?:'}), required=True, max_length=50)
    stock = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'How many do you have?:'}), required=True, max_length=50)
    price = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter rate:'}), required=True, max_length=50)


    class Meta():
        model = products
        fields = ['name', 'stock', 'price']

