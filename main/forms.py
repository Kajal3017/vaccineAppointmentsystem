from django import forms
from django.core.validators import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings
from django.forms.widgets import DateInput


from .models import Vaccine, Clinic, UserAppointBooking

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

    def __init__(self,  *args, **kwargs):
        # self.request = kwargs.pop('request')
        super(VaccineForm, self).__init__(*args, **kwargs)

    def clean_vaccine_for(self):
        name = self.cleaned_data.get('vaccine_for')
        try:
            match = Vaccine.objects.get(vaccine_for=name)
        except Vaccine.DoesNotExist:
            return name
        raise ValidationError(_('The Location already exist. Please update the value instead adding new.'))

    class Meta:
        model = Vaccine
        fields = ['vaccine_for', 'vaccine_name', 'quantity', 'clinic']


class ClinicForm(forms.ModelForm):

    # def __init__(self,  *args, **kwargs):
    #     self.request = kwargs.pop('request')
    #     super(ClinicForm, self).__init__(*args, **kwargs)

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        is_number = phone_number.isnumeric()

        if not is_number:
            raise ValidationError(_('The value must be a number.'))
        elif len(phone_number) != 10:
            raise ValidationError(_('The value can not be less than or greater than 10.'))
        else:
            return phone_number

    def clean_clinic_name(self):
        name = self.cleaned_data.get('clinic_name')
        try:
            match = Clinic.objects.get(clinic_name=name)
        except Clinic.DoesNotExist:
            return name
        raise ValidationError(_('The Clinic already exist. Please update the value instead adding new.'))
    class Meta:
        model = Clinic
        fields = ['clinic_name', 'address_line_one', 'address_line_two', 'postal_code', 'city', 'provinces',
        'phone_code', 'phone_number', 'website', 'opening_time', 'closing_time']

        widgets = {
                'closing_time': forms.TimeInput(format='%H:%M'),
            }



class UserAppointBookingForm(forms.ModelForm):

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        is_number = phone_number.isnumeric()
        if not is_number:
            raise ValidationError(_('The value must be a number.'))
        elif is_number != 10:
            raise ValidationError(_('The value can not be less than or greater than 10.'))
        else:
            return phone_number

    class Meta:
        widgets = {
            'DOB': DateInput()
        }
        model = UserAppointBooking
        fields = ['first_name', 'last_name', 'address_line_one', 'address_line_two', 'postal_code', 'city', 'provinces',
        'phone_code', 'phone_number', 'DOB', 'gender', 'health_card', 'which_dose', 'vaccine_name', 'choose_date']

       


        