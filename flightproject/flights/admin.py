from django.contrib import admin
from .models import Country , AirlineCompany, Flight, Ticket
# Register your models here.

admin.site.register(Country)
admin.site.register(AirlineCompany)
admin.site.register(Flight)
admin.site.register(Ticket)

