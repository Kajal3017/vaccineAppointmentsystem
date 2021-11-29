from django.contrib import admin

from .models import Vaccine, Clinic


admin.site.register(Vaccine)
admin.site.register(Clinic)
