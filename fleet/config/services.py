from .models import (
    VehicleCategory, VehicleType, FuelType, Transmission, TractionType,
    UnitCategory, Unit, ActivitySector, Period, InterventionType,
    DocumentType, Tag,
)


# ---------------------------------------------------------------------------
# VehicleCategory
# ---------------------------------------------------------------------------
def create_vehicle_category(*, name: str, created_by=None) -> VehicleCategory:
    return VehicleCategory.objects.create(name=name, created_by=created_by)


def update_vehicle_category(*, instance: VehicleCategory, name: str) -> VehicleCategory:
    instance.name = name
    instance.save(update_fields=["name", "updated_at"])
    return instance


def delete_vehicle_category(*, instance: VehicleCategory) -> None:
    instance.delete()


# ---------------------------------------------------------------------------
# VehicleType
# ---------------------------------------------------------------------------
def create_vehicle_type(*, name: str, created_by=None) -> VehicleType:
    return VehicleType.objects.create(name=name, created_by=created_by)


def update_vehicle_type(*, instance: VehicleType, name: str) -> VehicleType:
    instance.name = name
    instance.save(update_fields=["name", "updated_at"])
    return instance


def delete_vehicle_type(*, instance: VehicleType) -> None:
    instance.delete()


# ---------------------------------------------------------------------------
# FuelType
# ---------------------------------------------------------------------------
def create_fuel_type(*, name: str, created_by=None) -> FuelType:
    return FuelType.objects.create(name=name, created_by=created_by)


def update_fuel_type(*, instance: FuelType, name: str) -> FuelType:
    instance.name = name
    instance.save(update_fields=["name", "updated_at"])
    return instance


def delete_fuel_type(*, instance: FuelType) -> None:
    instance.delete()


# ---------------------------------------------------------------------------
# Transmission
# ---------------------------------------------------------------------------
def create_transmission(*, name: str, created_by=None) -> Transmission:
    return Transmission.objects.create(name=name, created_by=created_by)


def update_transmission(*, instance: Transmission, name: str) -> Transmission:
    instance.name = name
    instance.save(update_fields=["name", "updated_at"])
    return instance


def delete_transmission(*, instance: Transmission) -> None:
    instance.delete()


# ---------------------------------------------------------------------------
# TractionType
# ---------------------------------------------------------------------------
def create_traction_type(*, name: str, created_by=None) -> TractionType:
    return TractionType.objects.create(name=name, created_by=created_by)


def update_traction_type(*, instance: TractionType, name: str) -> TractionType:
    instance.name = name
    instance.save(update_fields=["name", "updated_at"])
    return instance


def delete_traction_type(*, instance: TractionType) -> None:
    instance.delete()


# ---------------------------------------------------------------------------
# UnitCategory
# ---------------------------------------------------------------------------
def create_unit_category(*, name: str, created_by=None) -> UnitCategory:
    return UnitCategory.objects.create(name=name, created_by=created_by)


def update_unit_category(*, instance: UnitCategory, name: str) -> UnitCategory:
    instance.name = name
    instance.save(update_fields=["name", "updated_at"])
    return instance


def delete_unit_category(*, instance: UnitCategory) -> None:
    instance.delete()


# ---------------------------------------------------------------------------
# Unit
# ---------------------------------------------------------------------------
def create_unit(*, category_id, code: str, name: str, created_by=None) -> Unit:
    return Unit.objects.create(
        category_id=category_id, code=code, name=name, created_by=created_by
    )


def update_unit(*, instance: Unit, data: dict) -> Unit:
    allowed = ["category_id", "code", "name"]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    return instance


def delete_unit(*, instance: Unit) -> None:
    instance.delete()


# ---------------------------------------------------------------------------
# ActivitySector
# ---------------------------------------------------------------------------
def create_activity_sector(*, code: str, name: str, created_by=None) -> ActivitySector:
    return ActivitySector.objects.create(code=code, name=name, created_by=created_by)


def update_activity_sector(*, instance: ActivitySector, data: dict) -> ActivitySector:
    allowed = ["code", "name"]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    return instance


def delete_activity_sector(*, instance: ActivitySector) -> None:
    instance.delete()


# ---------------------------------------------------------------------------
# Period
# ---------------------------------------------------------------------------
def create_period(*, name: str, created_by=None) -> Period:
    return Period.objects.create(name=name, created_by=created_by)


def update_period(*, instance: Period, name: str) -> Period:
    instance.name = name
    instance.save(update_fields=["name", "updated_at"])
    return instance


def delete_period(*, instance: Period) -> None:
    instance.delete()


# ---------------------------------------------------------------------------
# InterventionType
# ---------------------------------------------------------------------------
def create_intervention_type(*, name: str, category: str, created_by=None) -> InterventionType:
    return InterventionType.objects.create(name=name, category=category, created_by=created_by)


def update_intervention_type(*, instance: InterventionType, data: dict) -> InterventionType:
    allowed = ["name", "category"]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    return instance


def delete_intervention_type(*, instance: InterventionType) -> None:
    instance.delete()


# ---------------------------------------------------------------------------
# DocumentType
# ---------------------------------------------------------------------------
def create_document_type(*, code: str, label: str, requires_expiration: bool = True, created_by=None) -> DocumentType:
    return DocumentType.objects.create(
        code=code, label=label, requires_expiration=requires_expiration, created_by=created_by
    )


def update_document_type(*, instance: DocumentType, data: dict) -> DocumentType:
    allowed = ["code", "label", "requires_expiration"]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    return instance


def delete_document_type(*, instance: DocumentType) -> None:
    instance.delete()


# ---------------------------------------------------------------------------
# Tag
# ---------------------------------------------------------------------------
def create_tag(*, name: str, color: str = "", created_by=None) -> Tag:
    return Tag.objects.create(name=name, color=color, created_by=created_by)


def update_tag(*, instance: Tag, data: dict) -> Tag:
    allowed = ["name", "color"]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    return instance


def delete_tag(*, instance: Tag) -> None:
    instance.delete()
