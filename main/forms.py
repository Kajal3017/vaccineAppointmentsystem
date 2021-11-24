from django import forms
from django.contrib.auth.models import User
from django.conf import settings

from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

from .models import Vaccine, BookingFormINFO

class DashboardForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DashboardForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }
        fields = ['username', 'email', 'first_name', 'last_name']


class VaccineForm(forms.ModelForm):

    class Meta:
        model = Vaccine
        fields = ['vaccine_name', 'quantity']


class BookingFormINFOForm(forms.ModelForm):

    class Meta:
        model = BookingFormINFO
        fields = ['vaccine', 'clinic_name', 'address_line_one', 'address_line_two', 'postal_code', 'city', 'provinces',
        'phone_code', 'phone_number', 'website', 'opening_time', 'closing_time']

    widgets = {
            'opening_time': TimePicker(),
            'closing_time': forms.TimeInput(format='%H:%M'),
        }

        