from django.urls import path, include
from . import views

app_name = "vehicles"

urlpatterns = [
    # --- VehicleModel ---
    path("models/", views.VehicleModelListView.as_view(), name="vehicle-model-list"),
    path("models/<uuid:pk>/", views.VehicleModelDetailView.as_view(), name="vehicle-model-detail"),
    path("models/create/", views.VehicleModelCreateView.as_view(), name="vehicle-model-create"),
    path("models/<uuid:pk>/edit/", views.VehicleModelUpdateView.as_view(), name="vehicle-model-update"),
    path("models/<uuid:pk>/delete/", views.VehicleModelDeleteView.as_view(), name="vehicle-model-delete"),

    # --- Parking ---
    path("parkings/", views.ParkingListView.as_view(), name="parking-list"),
    path("parkings/<uuid:pk>/", views.ParkingDetailView.as_view(), name="parking-detail"),
    path("parkings/create/", views.ParkingCreateView.as_view(), name="parking-create"),
    path("parkings/<uuid:pk>/edit/", views.ParkingUpdateView.as_view(), name="parking-update"),
    path("parkings/<uuid:pk>/delete/", views.ParkingDeleteView.as_view(), name="parking-delete"),

    # --- Vehicle ---
    path("", views.VehicleListView.as_view(), name="vehicle-list"),
    path("<uuid:pk>/", views.VehicleDetailView.as_view(), name="vehicle-detail"),
    path("create/", views.VehicleCreateView.as_view(), name="vehicle-create"),
    path("<uuid:pk>/edit/", views.VehicleUpdateView.as_view(), name="vehicle-update"),
    path("<uuid:pk>/delete/", views.VehicleDeleteView.as_view(), name="vehicle-delete"),

    # --- OdometerReading (nested under vehicle) ---
    path("<uuid:vehicle_pk>/odometer/", views.OdometerReadingListView.as_view(), name="odometer-list"),
    path("<uuid:vehicle_pk>/odometer/add/", views.OdometerReadingCreateView.as_view(), name="odometer-create"),
    path("odometer/<uuid:pk>/", views.OdometerReadingDetailView.as_view(), name="odometer-detail"),
    path("odometer/<uuid:pk>/edit/", views.OdometerReadingUpdateView.as_view(), name="odometer-update"),
    path("odometer/<uuid:pk>/delete/", views.OdometerReadingDeleteView.as_view(), name="odometer-delete"),

    # --- VehicleDocument (nested under vehicle) ---
    path("<uuid:vehicle_pk>/documents/", views.VehicleDocumentListView.as_view(), name="vehicle-document-list"),
    path("<uuid:vehicle_pk>/documents/add/", views.VehicleDocumentCreateView.as_view(), name="vehicle-document-create"),
    path("documents/<uuid:pk>/", views.VehicleDocumentDetailView.as_view(), name="vehicle-document-detail"),
    path("documents/<uuid:pk>/edit/", views.VehicleDocumentUpdateView.as_view(), name="vehicle-document-update"),
    path("documents/<uuid:pk>/delete/", views.VehicleDocumentDeleteView.as_view(), name="vehicle-document-delete"),

    # --- VehicleLayout (nested under vehicle) ---
    path("<uuid:vehicle_pk>/layouts/", views.VehicleLayoutListView.as_view(), name="vehicle-layout-list"),
    path("<uuid:vehicle_pk>/layouts/add/", views.VehicleLayoutCreateView.as_view(), name="vehicle-layout-create"),
    path("layouts/<uuid:pk>/", views.VehicleLayoutDetailView.as_view(), name="vehicle-layout-detail"),
    path("layouts/<uuid:pk>/edit/", views.VehicleLayoutUpdateView.as_view(), name="vehicle-layout-update"),
    path("layouts/<uuid:pk>/delete/", views.VehicleLayoutDeleteView.as_view(), name="vehicle-layout-delete"),

    # --- Seat (nested under layout) ---
    path("layouts/<uuid:layout_pk>/seats/", views.SeatListView.as_view(), name="seat-list"),
    path("layouts/<uuid:layout_pk>/seats/add/", views.SeatCreateView.as_view(), name="seat-create"),
    path("seats/<uuid:pk>/", views.SeatDetailView.as_view(), name="seat-detail"),
    path("seats/<uuid:pk>/edit/", views.SeatUpdateView.as_view(), name="seat-update"),
    path("seats/<uuid:pk>/delete/", views.SeatDeleteView.as_view(), name="seat-delete"),

    # --- API ---
    path("api/", include("fleet.vehicles.api.urls")),
]
