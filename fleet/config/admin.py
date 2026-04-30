from django.contrib import admin

from .models import *

my_models = [ VehicleCategory, VehicleType, FuelType, Transmission, TractionType,
    UnitCategory, Unit, ActivitySector, Period, InterventionType,
    DocumentType, Tag ]


admin.site.register(my_models)