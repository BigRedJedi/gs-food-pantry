from django import forms
from .models import Client, Item, Employee, Donor, Visit

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'address', 'client_number', 'city', 'state', 'zipcode', 'email', 'cell_phone',)


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'item_number', 'item_type', 'description', 'qty_on_hand', 'expired_date',)


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'address', 'emp_number', 'city', 'state', 'zipcode', 'email', 'cell_phone',)


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('name', 'address', 'donor_number', 'city', 'state', 'zipcode', 'email', 'cell_phone',)