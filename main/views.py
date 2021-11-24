from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from main.forms import DashboardForm, VaccineForm, BookingFormINFOForm


def index(request):
    return HttpResponse("This is going to be the landing page.")


def add_clinic_info(request):
    form = BookingFormINFOForm()
    if request.method == 'POST' or None:
        form = BookingFormINFOForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Clinic info added.')
            return redirect('index')

    dictionary = {'form': form}
    return render(request, 'main/clinic_tem.html', dictionary)


def add_vaccine(request):
    form = VaccineForm()
    if request.method == 'POST' or None:
        form = VaccineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vaccine quantity added.')
            return redirect('index')

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
    