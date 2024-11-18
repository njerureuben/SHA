from django.contrib import admin

from application.models import Appointment, Contact

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Contact)