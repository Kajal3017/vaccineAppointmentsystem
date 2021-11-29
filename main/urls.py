from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    
    path('donation/', views.donation, name="donation"),
    path('payment/success/', views.success, name='success'),
    path('payment/cancel/', views.cancel, name='cancel'),
    path('create-checkout-session/', views.create_checkout_session, name="create_checkout_session"),

    path('clinic/list/', views.clinin_list, name='clinic_list'),
    path('add/vaccine/', views.add_vaccine, name='add_vaccine'),

    path('add/clinic/', views.add_clinic_info, name='add_clinic_info'),
    path('edit/clinic?id=<clinic_id>/', views.edit_clinic, name='edit_clinic'),
    path('confirm/delete/clinic?id=<clinic_id>/', views.delete_clinic, name='delete_clinic'),
    path('delete/clinic?id=<clinic_id>/', views.delete_it_clinic, name='delete_it_clinic'),
    
    path('book/appointment/', views.book_appointment_view, name='book_appointment'),
    path('user=<user_name>/', views.dashboard, name='dashboard'),
]