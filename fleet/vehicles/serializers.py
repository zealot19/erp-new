from rest_framework import serializers
from .models import VehicleModel, Parking, Vehicle, OdometerReading, VehicleDocument, VehicleLayout, Seat


# ---------------------------------------------------------------------------
# VehicleModel
# ---------------------------------------------------------------------------
class VehicleModelListSerializer(serializers.ModelSerializer):
    manufacturer_name = serializers.CharField(source="manufacturer.name", read_only=True)
    vehicle_type_name = serializers.CharField(source="vehicle_type.name", read_only=True)

    class Meta:
        model = VehicleModel
        fields = ["id", "manufacturer", "manufacturer_name", "name", "model_year", "vehicle_type", "vehicle_type_name"]


class VehicleModelDetailSerializer(serializers.ModelSerializer):
    manufacturer_name = serializers.CharField(source="manufacturer.name", read_only=True)
    vehicle_type_name = serializers.CharField(source="vehicle_type.name", read_only=True)
    fuel_type_name = serializers.CharField(source="fuel_type.name", read_only=True)
    transmission_name = serializers.CharField(source="transmission.name", read_only=True)
    traction_type_name = serializers.CharField(source="traction_type.name", read_only=True)
    power_unit_code = serializers.CharField(source="power_unit.code", read_only=True, default=None)
    range_unit_code = serializers.CharField(source="range_unit.code", read_only=True, default=None)
    emission_unit_code = serializers.CharField(source="emission_unit.code", read_only=True, default=None)

    class Meta:
        model = VehicleModel
        fields = [
            "id", "image", "vehicle_type", "vehicle_type_name",
            "manufacturer", "manufacturer_name", "name", "model_year",
            "seats", "doors", "color", "has_tow_hitch",
            "fuel_type", "fuel_type_name", "transmission", "transmission_name",
            "traction_type", "traction_type_name",
            "power", "power_unit", "power_unit_code",
            "range_value", "range_unit", "range_unit_code",
            "co2_emission", "emission_unit", "emission_unit_code", "emission_standard",
            "suppliers", "created_at", "updated_at",
        ]


# ---------------------------------------------------------------------------
# Parking
# ---------------------------------------------------------------------------
class ParkingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ["id", "name", "location"]


class ParkingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ["id", "name", "location", "notes", "created_at", "updated_at"]


# ---------------------------------------------------------------------------
# Vehicle
# ---------------------------------------------------------------------------
class VehicleListSerializer(serializers.ModelSerializer):
    model_display = serializers.CharField(source="vehicle_model.__str__", read_only=True)
    driver_name = serializers.CharField(source="driver.full_name", read_only=True, default=None)
    state_display = serializers.CharField(source="get_state_display", read_only=True)

    class Meta:
        model = Vehicle
        fields = [
            "id", "license_plate", "vin", "vehicle_model", "model_display",
            "category", "driver", "driver_name", "state", "state_display",
        ]


class VehicleDetailSerializer(serializers.ModelSerializer):
    model_display = serializers.CharField(source="vehicle_model.__str__", read_only=True)
    driver_name = serializers.CharField(source="driver.full_name", read_only=True, default=None)
    state_display = serializers.CharField(source="get_state_display", read_only=True)
    parking_name = serializers.CharField(source="parking.name", read_only=True, default=None)
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Vehicle
        fields = [
            "id", "license_plate", "vin",
            "vehicle_model", "model_display",
            "category", "category_name",
            "driver", "driver_name",
            "fleet_manager", "tags",
            "parking", "parking_name",
            "order_date", "registration_date", "cancellation_date", "first_contract_date",
            "fiscal_horsepower", "catalog_value", "purchase_value", "residual_value",
            "state", "state_display", "notes",
            "created_at", "updated_at",
        ]


# ---------------------------------------------------------------------------
# OdometerReading
# ---------------------------------------------------------------------------
class OdometerReadingListSerializer(serializers.ModelSerializer):
    unit_code = serializers.CharField(source="unit.code", read_only=True)

    class Meta:
        model = OdometerReading
        fields = ["id", "vehicle", "date", "value", "unit", "unit_code"]


class OdometerReadingDetailSerializer(serializers.ModelSerializer):
    unit_code = serializers.CharField(source="unit.code", read_only=True)
    vehicle_plate = serializers.CharField(source="vehicle.license_plate", read_only=True)

    class Meta:
        model = OdometerReading
        fields = [
            "id", "vehicle", "vehicle_plate", "date", "value",
            "unit", "unit_code", "notes", "created_at", "updated_at",
        ]


# ---------------------------------------------------------------------------
# VehicleDocument
# ---------------------------------------------------------------------------
class VehicleDocumentListSerializer(serializers.ModelSerializer):
    document_type_label = serializers.CharField(source="document_type.label", read_only=True)
    status_display = serializers.CharField(source="get_status_display", read_only=True)
    is_expired = serializers.BooleanField(read_only=True)

    class Meta:
        model = VehicleDocument
        fields = [
            "id", "vehicle", "document_type", "document_type_label",
            "reference_number", "expiry_date", "status", "status_display", "is_expired",
        ]


class VehicleDocumentDetailSerializer(serializers.ModelSerializer):
    document_type_label = serializers.CharField(source="document_type.label", read_only=True)
    status_display = serializers.CharField(source="get_status_display", read_only=True)
    is_expired = serializers.BooleanField(read_only=True)
    vehicle_plate = serializers.CharField(source="vehicle.license_plate", read_only=True)

    class Meta:
        model = VehicleDocument
        fields = [
            "id", "document_type", "document_type_label",
            "vehicle", "vehicle_plate",
            "reference_number", "issue_date", "expiry_date",
            "file", "status", "status_display", "is_expired",
            "created_at", "updated_at",
        ]


# ---------------------------------------------------------------------------
# VehicleLayout
# ---------------------------------------------------------------------------
class VehicleLayoutListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleLayout
        fields = ["id", "vehicle", "name", "total_seats", "is_active"]


class VehicleLayoutDetailSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.CharField(source="vehicle.license_plate", read_only=True)

    class Meta:
        model = VehicleLayout
        fields = [
            "id", "vehicle", "vehicle_plate", "name",
            "total_seats", "is_active", "created_at", "updated_at",
        ]


# ---------------------------------------------------------------------------
# Seat
# ---------------------------------------------------------------------------
class SeatListSerializer(serializers.ModelSerializer):
    seat_type_display = serializers.CharField(source="get_seat_type_display", read_only=True)

    class Meta:
        model = Seat
        fields = ["id", "layout", "seat_number", "row", "column", "seat_type", "seat_type_display", "is_available"]


class SeatDetailSerializer(serializers.ModelSerializer):
    seat_type_display = serializers.CharField(source="get_seat_type_display", read_only=True)

    class Meta:
        model = Seat
        fields = [
            "id", "layout", "seat_number", "row", "column",
            "seat_type", "seat_type_display", "is_available",
            "created_at", "updated_at",
        ]
