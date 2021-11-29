from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from main.forms import DashboardForm, VaccineForm, ClinicForm, UserAppointBookingForm
from main.models import UserAppointBooking, Clinic, Vaccine

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


import stripe
stripe.api_key = "sk_test_51K0oHcEJY1gb5QocIhDuq1W5WFKbVo59IIF7OrjNW6mWPzctGdIrhURc58koLaKhfP35NR09qlQZYFajpUyZFAnn00j2O6vh1l"
YOUR_DOMAIN = 'http://localhost:8000/'
def create_checkout_session(request):
    if request.method == 'POST':
        checkout_session = stripe.checkout.Session.create(
            # payment_method_types=['card'],
            line_items=[
                {
                    # Provide the exact Price ID (e.g. pr_1234) of the product you want to sell
                    'price': 'price_1K0upkEJY1gb5Qocr2Luy6Ym',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + 'payment/success/',
            cancel_url=YOUR_DOMAIN + 'payment/cancel/',
        )
    return redirect(checkout_session.url)


def donation(request):
    return render(request, 'main/checkout.html')

    
def success(request):
    return render(request, 'main/success.html')
    
def cancel(request):
    return render(request, 'main/cancel.html')


def index(request):
    return render(request, 'main/homepage.html', {})


def clinin_list(request):
    clinic_list = Clinic.objects.all()
    return render(request, 'main/clinic_list.html', {'clinic_list': clinic_list})

def delete_clinic(request, clinic_id):
    clinic = get_object_or_404(Clinic, pk=clinic_id)
    return render(request, 'main/confirm_delete.html', {'clinic': clinic})


def delete_it_clinic(request, clinic_id):
    clinic = get_object_or_404(Clinic, pk=clinic_id)
    clinic.delete()
    return redirect('clinic_list')


def edit_clinic(request, clinic_id):
    clinic = get_object_or_404(Clinic, pk=clinic_id)
    form = ClinicForm(instance=clinic)
    if request.method == 'POST':
        form = ClinicForm(request.POST, instance=clinic)
        if form.is_valid():
            form.save()
            messages.info(request, 'Clinic information updated.')
            return redirect('clinic_list')

    dictionary = {'form': form}
    return render(request, 'main/clinic_tem.html', dictionary) 


@login_required
def book_appointment_view(request):
    form = UserAppointBookingForm()
    if request.method == 'POST' or None:
        form = UserAppointBookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your appointment is booked.')
            return redirect('index')

    dictionary = {'form': form}
    return render(request, 'main/book_appointment.html', dictionary)


@login_required
def add_clinic_info(request):
    if not request.user.is_superuser:
        raise PermissionDenied()
    form = ClinicForm()
    if request.method == 'POST' or None:
        form = ClinicForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Clinic info added.')
            return redirect('book_appointment')

    dictionary = {'form': form}
    return render(request, 'main/clinic_tem.html', dictionary)


@login_required
def add_vaccine(request):
    if not request.user.is_superuser:
        raise PermissionDenied()
    form = VaccineForm()
    if request.method == 'POST' or None:
        form = VaccineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vaccine quantity added.')
            return redirect('add_clinic_info')

    dictionary = {'form': form}
    return render(request, 'main/add_vaccine.html', dictionary)


def dashboard(request, user_name):
    user = User.objects.get(username=user_name)

    password_form = PasswordChangeForm(request.user)
    form = DashboardForm(instance=user)    
    if 'edit_profile' in request.POST and request.method == 'POST':
        form = DashboardForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfuly.')
            return redirect(reverse('dashboard', args=[user.username]))

    elif 'change_password' in request.POST and request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfuly.')
            return redirect(reverse('dashboard', args=[user.username]))

    dictionary = {'form': form, 'password_form': password_form}
    return render(request, 'main/dashboard.html', dictionary)
    