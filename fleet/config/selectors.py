from django.db.models import QuerySet
from .models import (
    VehicleCategory, VehicleType, FuelType, Transmission, TractionType,
    UnitCategory, Unit, ActivitySector, Period, InterventionType,
    DocumentType, Tag,
)


# ---------------------------------------------------------------------------
# VehicleCategory
# ---------------------------------------------------------------------------
def get_all_vehicle_categories() -> QuerySet:
    return VehicleCategory.objects.all()


def get_vehicle_category_by_id(*, category_id) -> VehicleCategory:
    return VehicleCategory.objects.get(id=category_id)


# ---------------------------------------------------------------------------
# VehicleType
# ---------------------------------------------------------------------------
def get_all_vehicle_types() -> QuerySet:
    return VehicleType.objects.all()


def get_vehicle_type_by_id(*, type_id) -> VehicleType:
    return VehicleType.objects.get(id=type_id)


# ---------------------------------------------------------------------------
# FuelType
# ---------------------------------------------------------------------------
def get_all_fuel_types() -> QuerySet:
    return FuelType.objects.all()


def get_fuel_type_by_id(*, fuel_type_id) -> FuelType:
    return FuelType.objects.get(id=fuel_type_id)


# ---------------------------------------------------------------------------
# Transmission
# ---------------------------------------------------------------------------
def get_all_transmissions() -> QuerySet:
    return Transmission.objects.all()


def get_transmission_by_id(*, transmission_id) -> Transmission:
    return Transmission.objects.get(id=transmission_id)


# ---------------------------------------------------------------------------
# TractionType
# ---------------------------------------------------------------------------
def get_all_traction_types() -> QuerySet:
    return TractionType.objects.all()


def get_traction_type_by_id(*, traction_type_id) -> TractionType:
    return TractionType.objects.get(id=traction_type_id)


# ---------------------------------------------------------------------------
# UnitCategory
# ---------------------------------------------------------------------------
def get_all_unit_categories() -> QuerySet:
    return UnitCategory.objects.all()


def get_unit_category_by_id(*, unit_category_id) -> UnitCategory:
    return UnitCategory.objects.get(id=unit_category_id)


# ---------------------------------------------------------------------------
# Unit
# ---------------------------------------------------------------------------
def get_all_units() -> QuerySet:
    return Unit.objects.select_related("category").all()


def get_units_by_category(*, category_id) -> QuerySet:
    return Unit.objects.select_related("category").filter(category_id=category_id)


def get_unit_by_id(*, unit_id) -> Unit:
    return Unit.objects.select_related("category").get(id=unit_id)


def get_unit_by_code(*, code: str) -> Unit:
    return Unit.objects.get(code=code)


# ---------------------------------------------------------------------------
# ActivitySector
# ---------------------------------------------------------------------------
def get_all_activity_sectors() -> QuerySet:
    return ActivitySector.objects.all()


def get_activity_sector_by_id(*, sector_id) -> ActivitySector:
    return ActivitySector.objects.get(id=sector_id)


# ---------------------------------------------------------------------------
# Period
# ---------------------------------------------------------------------------
def get_all_periods() -> QuerySet:
    return Period.objects.all()


def get_period_by_id(*, period_id) -> Period:
    return Period.objects.get(id=period_id)


# ---------------------------------------------------------------------------
# InterventionType
# ---------------------------------------------------------------------------
def get_all_intervention_types() -> QuerySet:
    return InterventionType.objects.all()


def get_intervention_types_by_category(*, category: str) -> QuerySet:
    return InterventionType.objects.filter(category=category)


def get_intervention_type_by_id(*, intervention_type_id) -> InterventionType:
    return InterventionType.objects.get(id=intervention_type_id)


# ---------------------------------------------------------------------------
# DocumentType
# ---------------------------------------------------------------------------
def get_all_document_types() -> QuerySet:
    return DocumentType.objects.all()


def get_document_types_requiring_expiration() -> QuerySet:
    return DocumentType.objects.filter(requires_expiration=True)


def get_document_type_by_id(*, document_type_id) -> DocumentType:
    return DocumentType.objects.get(id=document_type_id)


# ---------------------------------------------------------------------------
# Tag
# ---------------------------------------------------------------------------
def get_all_tags() -> QuerySet:
    return Tag.objects.all()


def get_tag_by_id(*, tag_id) -> Tag:
    return Tag.objects.get(id=tag_id)


def search_tags(*, name: str) -> QuerySet:
    return Tag.objects.filter(name__icontains=name)
