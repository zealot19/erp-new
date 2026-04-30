import datetime
from django.db.models import QuerySet
from .models import VehicleModel, Parking, Vehicle, OdometerReading, VehicleDocument, VehicleLayout, Seat


# ---------------------------------------------------------------------------
# VehicleModel
# ---------------------------------------------------------------------------
def get_all_vehicle_models() -> QuerySet:
    return VehicleModel.objects.select_related(
        "vehicle_type", "manufacturer", "fuel_type", "transmission", "traction_type"
    ).all()


def get_vehicle_models_by_manufacturer(*, manufacturer_id) -> QuerySet:
    return VehicleModel.objects.select_related(
        "vehicle_type", "manufacturer", "fuel_type", "transmission", "traction_type"
    ).filter(manufacturer_id=manufacturer_id)


def get_vehicle_model_by_id(*, vehicle_model_id) -> VehicleModel:
    return VehicleModel.objects.select_related(
        "vehicle_type", "manufacturer", "fuel_type", "transmission", "traction_type",
        "power_unit", "range_unit", "emission_unit",
    ).get(id=vehicle_model_id)


# ---------------------------------------------------------------------------
# Parking
# ---------------------------------------------------------------------------
def get_all_parkings() -> QuerySet:
    return Parking.objects.all()


def get_parking_by_id(*, parking_id) -> Parking:
    return Parking.objects.get(id=parking_id)


# ---------------------------------------------------------------------------
# Vehicle
# ---------------------------------------------------------------------------
def get_all_vehicles() -> QuerySet:
    return Vehicle.objects.select_related(
        "vehicle_model__manufacturer", "category", "driver", "parking"
    ).prefetch_related("tags").all()


def get_vehicles_by_state(*, state: str) -> QuerySet:
    return Vehicle.objects.select_related(
        "vehicle_model__manufacturer", "category", "driver", "parking"
    ).filter(state=state)


def get_vehicles_by_driver(*, driver_id) -> QuerySet:
    return Vehicle.objects.select_related(
        "vehicle_model__manufacturer", "category", "driver", "parking"
    ).filter(driver_id=driver_id)


def get_vehicles_by_parking(*, parking_id) -> QuerySet:
    return Vehicle.objects.filter(parking_id=parking_id)


def get_vehicle_by_id(*, vehicle_id) -> Vehicle:
    return Vehicle.objects.select_related(
        "vehicle_model__manufacturer", "vehicle_model__fuel_type",
        "category", "driver", "fleet_manager", "parking",
    ).prefetch_related("tags").get(id=vehicle_id)


def get_vehicle_by_plate(*, license_plate: str) -> Vehicle:
    return Vehicle.objects.get(license_plate=license_plate)


# ---------------------------------------------------------------------------
# OdometerReading
# ---------------------------------------------------------------------------
def get_odometer_readings_for_vehicle(*, vehicle_id) -> QuerySet:
    return OdometerReading.objects.select_related("unit").filter(vehicle_id=vehicle_id)


def get_latest_odometer_reading(*, vehicle_id) -> OdometerReading:
    return OdometerReading.objects.filter(vehicle_id=vehicle_id).select_related("unit").first()


def get_odometer_reading_by_id(*, reading_id) -> OdometerReading:
    return OdometerReading.objects.select_related("unit", "vehicle").get(id=reading_id)


# ---------------------------------------------------------------------------
# VehicleDocument
# ---------------------------------------------------------------------------
def get_documents_for_vehicle(*, vehicle_id) -> QuerySet:
    return VehicleDocument.objects.select_related("document_type").filter(vehicle_id=vehicle_id)


def get_expiring_documents(*, days: int = 30) -> QuerySet:
    threshold = datetime.date.today() + datetime.timedelta(days=days)
    return VehicleDocument.objects.select_related(
        "document_type", "vehicle"
    ).filter(
        expiry_date__lte=threshold,
        expiry_date__gte=datetime.date.today(),
        status=VehicleDocument.Status.ACTIVE,
    )


def get_expired_documents() -> QuerySet:
    return VehicleDocument.objects.select_related(
        "document_type", "vehicle"
    ).filter(
        expiry_date__lt=datetime.date.today(),
        status=VehicleDocument.Status.ACTIVE,
    )


def get_vehicle_document_by_id(*, document_id) -> VehicleDocument:
    return VehicleDocument.objects.select_related("document_type", "vehicle").get(id=document_id)


# ---------------------------------------------------------------------------
# VehicleLayout
# ---------------------------------------------------------------------------
def get_layouts_for_vehicle(*, vehicle_id) -> QuerySet:
    return VehicleLayout.objects.filter(vehicle_id=vehicle_id)


def get_active_layout_for_vehicle(*, vehicle_id) -> VehicleLayout:
    return VehicleLayout.objects.get(vehicle_id=vehicle_id, is_active=True)


def get_vehicle_layout_by_id(*, layout_id) -> VehicleLayout:
    return VehicleLayout.objects.select_related("vehicle").get(id=layout_id)


# ---------------------------------------------------------------------------
# Seat
# ---------------------------------------------------------------------------
def get_seats_for_layout(*, layout_id) -> QuerySet:
    return Seat.objects.filter(layout_id=layout_id)


def get_available_seats_for_layout(*, layout_id) -> QuerySet:
    return Seat.objects.filter(layout_id=layout_id, is_available=True)


def get_seat_by_id(*, seat_id) -> Seat:
    return Seat.objects.select_related("layout").get(id=seat_id)
