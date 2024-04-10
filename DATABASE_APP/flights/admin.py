from django.contrib import admin
from .models import Flights, Airport

# Register your models here.
admin.site.register(Flights)
admin.site.register(Airport)