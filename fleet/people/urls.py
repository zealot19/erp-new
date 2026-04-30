from django.urls import path, include
from . import views

app_name = "people"

urlpatterns = [
    # --- Driver ---
    path("drivers/", views.DriverListView.as_view(), name="driver-list"),
    path("drivers/<uuid:pk>/", views.DriverDetailView.as_view(), name="driver-detail"),
    path("drivers/create/", views.DriverCreateView.as_view(), name="driver-create"),
    path("drivers/<uuid:pk>/edit/", views.DriverUpdateView.as_view(), name="driver-update"),
    path("drivers/<uuid:pk>/delete/", views.DriverDeleteView.as_view(), name="driver-delete"),

    # --- Supplier ---
    path("suppliers/", views.SupplierListView.as_view(), name="supplier-list"),
    path("suppliers/<uuid:pk>/", views.SupplierDetailView.as_view(), name="supplier-detail"),
    path("suppliers/create/", views.SupplierCreateView.as_view(), name="supplier-create"),
    path("suppliers/<uuid:pk>/edit/", views.SupplierUpdateView.as_view(), name="supplier-update"),
    path("suppliers/<uuid:pk>/delete/", views.SupplierDeleteView.as_view(), name="supplier-delete"),

    # --- Manufacturer ---
    path("manufacturers/", views.ManufacturerListView.as_view(), name="manufacturer-list"),
    path("manufacturers/<uuid:pk>/", views.ManufacturerDetailView.as_view(), name="manufacturer-detail"),
    path("manufacturers/create/", views.ManufacturerCreateView.as_view(), name="manufacturer-create"),
    path("manufacturers/<uuid:pk>/edit/", views.ManufacturerUpdateView.as_view(), name="manufacturer-update"),
    path("manufacturers/<uuid:pk>/delete/", views.ManufacturerDeleteView.as_view(), name="manufacturer-delete"),

    # --- API ---
    path("api/", include("fleet.people.api.urls")),
]
