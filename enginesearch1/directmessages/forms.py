from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm,ReadOnlyPasswordHashField



# class MyForm(ModelForm)
#     class Meta:
#         model = MyModel
#         widgets = {
#           'summary': Textarea(attrs={'rows':80, 'cols':20}),
#         }

class Messageform(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows':5, 'cols':80}), required = True, max_length=600)

    class Meta():
        model = Message
        fields = [ 'recipient', 'content']