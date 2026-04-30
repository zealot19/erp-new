from django.urls import path, include
from . import views

app_name = "configuration"

urlpatterns = [
    # --- VehicleCategory ---
    path("vehicle-categories/", views.VehicleCategoryListView.as_view(), name="vehicle-category-list"),
    path("vehicle-categories/<uuid:pk>/", views.VehicleCategoryDetailView.as_view(), name="vehicle-category-detail"),
    path("vehicle-categories/create/", views.VehicleCategoryCreateView.as_view(), name="vehicle-category-create"),
    path("vehicle-categories/<uuid:pk>/edit/", views.VehicleCategoryUpdateView.as_view(), name="vehicle-category-update"),
    path("vehicle-categories/<uuid:pk>/delete/", views.VehicleCategoryDeleteView.as_view(), name="vehicle-category-delete"),

    # --- VehicleType ---
    path("vehicle-types/", views.VehicleTypeListView.as_view(), name="vehicle-type-list"),
    path("vehicle-types/<uuid:pk>/", views.VehicleTypeDetailView.as_view(), name="vehicle-type-detail"),
    path("vehicle-types/create/", views.VehicleTypeCreateView.as_view(), name="vehicle-type-create"),
    path("vehicle-types/<uuid:pk>/edit/", views.VehicleTypeUpdateView.as_view(), name="vehicle-type-update"),
    path("vehicle-types/<uuid:pk>/delete/", views.VehicleTypeDeleteView.as_view(), name="vehicle-type-delete"),

    # --- FuelType ---
    path("fuel-types/", views.FuelTypeListView.as_view(), name="fuel-type-list"),
    path("fuel-types/<uuid:pk>/", views.FuelTypeDetailView.as_view(), name="fuel-type-detail"),
    path("fuel-types/create/", views.FuelTypeCreateView.as_view(), name="fuel-type-create"),
    path("fuel-types/<uuid:pk>/edit/", views.FuelTypeUpdateView.as_view(), name="fuel-type-update"),
    path("fuel-types/<uuid:pk>/delete/", views.FuelTypeDeleteView.as_view(), name="fuel-type-delete"),

    # --- Transmission ---
    path("transmissions/", views.TransmissionListView.as_view(), name="transmission-list"),
    path("transmissions/<uuid:pk>/", views.TransmissionDetailView.as_view(), name="transmission-detail"),
    path("transmissions/create/", views.TransmissionCreateView.as_view(), name="transmission-create"),
    path("transmissions/<uuid:pk>/edit/", views.TransmissionUpdateView.as_view(), name="transmission-update"),
    path("transmissions/<uuid:pk>/delete/", views.TransmissionDeleteView.as_view(), name="transmission-delete"),

    # --- TractionType ---
    path("traction-types/", views.TractionTypeListView.as_view(), name="traction-type-list"),
    path("traction-types/<uuid:pk>/", views.TractionTypeDetailView.as_view(), name="traction-type-detail"),
    path("traction-types/create/", views.TractionTypeCreateView.as_view(), name="traction-type-create"),
    path("traction-types/<uuid:pk>/edit/", views.TractionTypeUpdateView.as_view(), name="traction-type-update"),
    path("traction-types/<uuid:pk>/delete/", views.TractionTypeDeleteView.as_view(), name="traction-type-delete"),

    # --- UnitCategory ---
    path("unit-categories/", views.UnitCategoryListView.as_view(), name="unit-category-list"),
    path("unit-categories/<uuid:pk>/", views.UnitCategoryDetailView.as_view(), name="unit-category-detail"),
    path("unit-categories/create/", views.UnitCategoryCreateView.as_view(), name="unit-category-create"),
    path("unit-categories/<uuid:pk>/edit/", views.UnitCategoryUpdateView.as_view(), name="unit-category-update"),
    path("unit-categories/<uuid:pk>/delete/", views.UnitCategoryDeleteView.as_view(), name="unit-category-delete"),

    # --- Unit ---
    path("units/", views.UnitListView.as_view(), name="unit-list"),
    path("units/<uuid:pk>/", views.UnitDetailView.as_view(), name="unit-detail"),
    path("units/create/", views.UnitCreateView.as_view(), name="unit-create"),
    path("units/<uuid:pk>/edit/", views.UnitUpdateView.as_view(), name="unit-update"),
    path("units/<uuid:pk>/delete/", views.UnitDeleteView.as_view(), name="unit-delete"),

    # --- ActivitySector ---
    path("activity-sectors/", views.ActivitySectorListView.as_view(), name="activity-sector-list"),
    path("activity-sectors/<uuid:pk>/", views.ActivitySectorDetailView.as_view(), name="activity-sector-detail"),
    path("activity-sectors/create/", views.ActivitySectorCreateView.as_view(), name="activity-sector-create"),
    path("activity-sectors/<uuid:pk>/edit/", views.ActivitySectorUpdateView.as_view(), name="activity-sector-update"),
    path("activity-sectors/<uuid:pk>/delete/", views.ActivitySectorDeleteView.as_view(), name="activity-sector-delete"),

    # --- Period ---
    path("periods/", views.PeriodListView.as_view(), name="period-list"),
    path("periods/<uuid:pk>/", views.PeriodDetailView.as_view(), name="period-detail"),
    path("periods/create/", views.PeriodCreateView.as_view(), name="period-create"),
    path("periods/<uuid:pk>/edit/", views.PeriodUpdateView.as_view(), name="period-update"),
    path("periods/<uuid:pk>/delete/", views.PeriodDeleteView.as_view(), name="period-delete"),

    # --- InterventionType ---
    path("intervention-types/", views.InterventionTypeListView.as_view(), name="intervention-type-list"),
    path("intervention-types/<uuid:pk>/", views.InterventionTypeDetailView.as_view(), name="intervention-type-detail"),
    path("intervention-types/create/", views.InterventionTypeCreateView.as_view(), name="intervention-type-create"),
    path("intervention-types/<uuid:pk>/edit/", views.InterventionTypeUpdateView.as_view(), name="intervention-type-update"),
    path("intervention-types/<uuid:pk>/delete/", views.InterventionTypeDeleteView.as_view(), name="intervention-type-delete"),

    # --- DocumentType ---
    path("document-types/", views.DocumentTypeListView.as_view(), name="document-type-list"),
    path("document-types/<uuid:pk>/", views.DocumentTypeDetailView.as_view(), name="document-type-detail"),
    path("document-types/create/", views.DocumentTypeCreateView.as_view(), name="document-type-create"),
    path("document-types/<uuid:pk>/edit/", views.DocumentTypeUpdateView.as_view(), name="document-type-update"),
    path("document-types/<uuid:pk>/delete/", views.DocumentTypeDeleteView.as_view(), name="document-type-delete"),

    # --- Tag ---
    path("tags/", views.TagListView.as_view(), name="tag-list"),
    path("tags/<uuid:pk>/", views.TagDetailView.as_view(), name="tag-detail"),
    path("tags/create/", views.TagCreateView.as_view(), name="tag-create"),
    path("tags/<uuid:pk>/edit/", views.TagUpdateView.as_view(), name="tag-update"),
    path("tags/<uuid:pk>/delete/", views.TagDeleteView.as_view(), name="tag-delete"),

    # --- API ---
    path("api/", include("fleet.config.api.urls")),
]
