from django.urls import path, include
from .views import *

urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('config/', include("fleet.config.urls")),
    path('vehicles/', include("fleet.vehicles.urls")),
    path('people/', include('fleet.people.urls')),
    path('operations/', include('fleet.operations.urls')),
]