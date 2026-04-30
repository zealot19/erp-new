from rest_framework import serializers
from .models import (
    VehicleCategory, VehicleType, FuelType, Transmission, TractionType,
    UnitCategory, Unit, ActivitySector, Period, InterventionType,
    DocumentType, Tag,
)


# ---------------------------------------------------------------------------
# VehicleCategory
# ---------------------------------------------------------------------------
class VehicleCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCategory
        fields = ["id", "name"]


class VehicleCategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCategory
        fields = ["id", "name", "created_at", "updated_at"]


# ---------------------------------------------------------------------------
# VehicleType
# ---------------------------------------------------------------------------
class VehicleTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ["id", "name"]


class VehicleTypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ["id", "name", "created_at", "updated_at"]


# ---------------------------------------------------------------------------
# FuelType
# ---------------------------------------------------------------------------
class FuelTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = ["id", "name"]


class FuelTypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = ["id", "name", "created_at", "updated_at"]


# ---------------------------------------------------------------------------
# Transmission
# ---------------------------------------------------------------------------
class TransmissionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmission
        fields = ["id", "name"]


class TransmissionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmission
        fields = ["id", "name", "created_at", "updated_at"]


# ---------------------------------------------------------------------------
# TractionType
# ---------------------------------------------------------------------------
class TractionTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TractionType
        fields = ["id", "name"]


class TractionTypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TractionType
        fields = ["id", "name", "created_at", "updated_at"]


# ---------------------------------------------------------------------------
# UnitCategory
# ---------------------------------------------------------------------------
class UnitCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitCategory
        fields = ["id", "name"]


class UnitCategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitCategory
        fields = ["id", "name", "created_at", "updated_at"]


# ---------------------------------------------------------------------------
# Unit
# ---------------------------------------------------------------------------
class UnitListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Unit
        fields = ["id", "code", "name", "category", "category_name"]


class UnitDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Unit
        fields = ["id", "code", "name", "category", "category_name", "created_at", "updated_at"]


# ---------------------------------------------------------------------------
# ActivitySector
# ---------------------------------------------------------------------------
class ActivitySectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivitySector
        fields = ["id", "code", "name"]


class ActivitySectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivitySector
        fields = ["id", "code", "name", "created_at", "updated_at"]


# ---------------------------------------------------------------------------
# Period
# ---------------------------------------------------------------------------
class PeriodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ["id", "name"]


class PeriodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ["id", "name", "created_at", "updated_at"]


# ---------------------------------------------------------------------------
# InterventionType
# ---------------------------------------------------------------------------
class InterventionTypeListSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source="get_category_display", read_only=True)

    class Meta:
        model = InterventionType
        fields = ["id", "name", "category", "category_display"]


class InterventionTypeDetailSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source="get_category_display", read_only=True)

    class Meta:
        model = InterventionType
        fields = ["id", "name", "category", "category_display", "created_at", "updated_at"]


# ---------------------------------------------------------------------------
# DocumentType
# ---------------------------------------------------------------------------
class DocumentTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ["id", "code", "label", "requires_expiration"]


class DocumentTypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ["id", "code", "label", "requires_expiration", "created_at", "updated_at"]


# ---------------------------------------------------------------------------
# Tag
# ---------------------------------------------------------------------------
class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "color"]


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "color", "created_at", "updated_at"]
