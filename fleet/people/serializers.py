from rest_framework import serializers
from .models import Driver, Supplier, Manufacturer


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
class DriverListSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = Driver
        fields = ["id", "full_name", "first_name", "last_name", "employee_id", "is_active"]


class DriverDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = Driver
        fields = [
            "id", "user", "employee_id", "first_name", "last_name",
            "full_name", "phone", "email", "license_number",
            "license_expiry", "license_category", "is_active",
            "created_at", "updated_at",
        ]


# ---------------------------------------------------------------------------
# Supplier
# ---------------------------------------------------------------------------
class SupplierListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["id", "code", "name", "city", "country", "is_active"]


class SupplierDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            "id", "name", "code", "tax_id", "address", "city", "country",
            "phone", "email", "website", "contact_person", "notes",
            "is_active", "created_at", "updated_at",
        ]


# ---------------------------------------------------------------------------
# Manufacturer
# ---------------------------------------------------------------------------
class ManufacturerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ["id", "name", "country", "logo"]


class ManufacturerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ["id", "name", "country", "logo", "created_at", "updated_at"]
