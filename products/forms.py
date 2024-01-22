# forms.py
from django import forms
from .models import ShippingAddress

class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['name', 'email', 'city', 'phone_number']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'اسم'}),
            'email': forms.EmailInput(attrs={'placeholder': 'بريد إلكتروني'}),
            'city': forms.TextInput(attrs={'placeholder': 'المدينة'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'هاتف'}),
        }
