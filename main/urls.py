from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('add/vaccine/', views.add_vaccine, name='add_vaccine'),
    path('add/clinic/', views.add_clinic_info, name='add_clinic_info'),
    path('user=<user_name>/', views.dashboard, name='dashboard'),
]