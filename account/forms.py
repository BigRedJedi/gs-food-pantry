from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('client_number', 'first_name', 'last_name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone')