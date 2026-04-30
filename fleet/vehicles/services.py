from .models import VehicleModel, Parking, Vehicle, OdometerReading, VehicleDocument, VehicleLayout, Seat


# ---------------------------------------------------------------------------
# VehicleModel
# ---------------------------------------------------------------------------
def create_vehicle_model(*, data: dict, created_by=None) -> VehicleModel:
    suppliers = data.pop("suppliers", [])
    instance = VehicleModel.objects.create(**data, created_by=created_by)
    if suppliers:
        instance.suppliers.set(suppliers)
    return instance


def update_vehicle_model(*, instance: VehicleModel, data: dict) -> VehicleModel:
    suppliers = data.pop("suppliers", None)
    allowed = [
        "image", "vehicle_type_id", "manufacturer_id", "name", "model_year",
        "seats", "doors", "color", "has_tow_hitch", "fuel_type_id",
        "transmission_id", "traction_type_id", "power", "power_unit_id",
        "range_value", "range_unit_id", "co2_emission", "emission_unit_id", "emission_standard",
    ]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    if suppliers is not None:
        instance.suppliers.set(suppliers)
    return instance


def delete_vehicle_model(*, instance: VehicleModel) -> None:
    instance.delete()


# ---------------------------------------------------------------------------
# Parking
# ---------------------------------------------------------------------------
def create_parking(*, name: str, location: str = "", notes: str = "", created_by=None) -> Parking:
    return Parking.objects.create(name=name, location=location, notes=notes, created_by=created_by)


def update_parking(*, instance: Parking, data: dict) -> Parking:
    allowed = ["name", "location", "notes"]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    return instance


def delete_parking(*, instance: Parking) -> None:
    instance.delete()


# ---------------------------------------------------------------------------
# Vehicle
# ---------------------------------------------------------------------------
def create_vehicle(*, data: dict, created_by=None) -> Vehicle:
    tags = data.pop("tags", [])
    instance = Vehicle.objects.create(**data, created_by=created_by)
    if tags:
        instance.tags.set(tags)
    return instance


def update_vehicle(*, instance: Vehicle, data: dict) -> Vehicle:
    tags = data.pop("tags", None)
    allowed = [
        "license_plate", "vin", "vehicle_model_id", "category_id",
        "driver_id", "fleet_manager_id", "parking_id",
        "order_date", "registration_date", "cancellation_date", "first_contract_date",
        "fiscal_horsepower", "catalog_value", "purchase_value", "residual_value",
        "state", "notes",
    ]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    if tags is not None:
        instance.tags.set(tags)
    return instance


def delete_vehicle(*, instance: Vehicle) -> None:
    instance.delete()


def change_vehicle_state(*, instance: Vehicle, state: str) -> Vehicle:
    instance.state = state
    instance.save(update_fields=["state", "updated_at"])
    return instance


def assign_driver(*, instance: Vehicle, driver_id) -> Vehicle:
    instance.driver_id = driver_id
    instance.save(update_fields=["driver_id", "updated_at"])
    return instance


def assign_parking(*, instance: Vehicle, parking_id) -> Vehicle:
    instance.parking_id = parking_id
    instance.save(update_fields=["parking_id", "updated_at"])
    return instance


# ---------------------------------------------------------------------------
# OdometerReading
# ---------------------------------------------------------------------------
def create_odometer_reading(*, data: dict, created_by=None) -> OdometerReading:
    return OdometerReading.objects.create(**data, created_by=created_by)


def update_odometer_reading(*, instance: OdometerReading, data: dict) -> OdometerReading:
    allowed = ["vehicle_id", "date", "value", "unit_id", "notes"]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    return instance


def delete_odometer_reading(*, instance: OdometerReading) -> None:
    instance.delete()


# ---------------------------------------------------------------------------
# VehicleDocument
# ---------------------------------------------------------------------------
def create_vehicle_document(*, data: dict, created_by=None) -> VehicleDocument:
    return VehicleDocument.objects.create(**data, created_by=created_by)


def update_vehicle_document(*, instance: VehicleDocument, data: dict) -> VehicleDocument:
    allowed = [
        "document_type_id", "vehicle_id", "reference_number",
        "issue_date", "expiry_date", "file", "status",
    ]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    return instance


def delete_vehicle_document(*, instance: VehicleDocument) -> None:
    instance.delete()


# ---------------------------------------------------------------------------
# VehicleLayout
# ---------------------------------------------------------------------------
def create_vehicle_layout(*, vehicle_id, name: str, total_seats: int, is_active: bool = False, created_by=None) -> VehicleLayout:
    return VehicleLayout.objects.create(
        vehicle_id=vehicle_id, name=name, total_seats=total_seats,
        is_active=is_active, created_by=created_by,
    )


def update_vehicle_layout(*, instance: VehicleLayout, data: dict) -> VehicleLayout:
    allowed = ["name", "total_seats", "is_active"]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    return instance


def delete_vehicle_layout(*, instance: VehicleLayout) -> None:
    instance.delete()


def activate_layout(*, instance: VehicleLayout) -> VehicleLayout:
    """Deactivates all other layouts for the vehicle, then activates this one."""
    VehicleLayout.objects.filter(vehicle=instance.vehicle).update(is_active=False)
    instance.is_active = True
    instance.save(update_fields=["is_active", "updated_at"])
    return instance


# ---------------------------------------------------------------------------
# Seat
# ---------------------------------------------------------------------------
def create_seat(*, data: dict, created_by=None) -> Seat:
    return Seat.objects.create(**data, created_by=created_by)


def update_seat(*, instance: Seat, data: dict) -> Seat:
    allowed = ["seat_number", "row", "column", "seat_type", "is_available"]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    return instance


def delete_seat(*, instance: Seat) -> None:
    instance.delete()
