from django import forms
from .models import Order, Visit


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['visit', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
