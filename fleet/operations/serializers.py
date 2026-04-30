from rest_framework import serializers
from .models import Service, ServiceAttachment, Contract, RecurringCost


# ---------------------------------------------------------------------------
# Service
# ---------------------------------------------------------------------------
class ServiceListSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.CharField(source="vehicle.license_plate", read_only=True)
    status_display = serializers.CharField(source="get_status_display", read_only=True)
    intervention_type_name = serializers.CharField(source="intervention_type.name", read_only=True)

    class Meta:
        model = Service
        fields = [
            "id", "vehicle", "vehicle_plate", "description",
            "intervention_type", "intervention_type_name",
            "date", "cost", "currency", "status", "status_display",
        ]


class ServiceDetailSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.CharField(source="vehicle.license_plate", read_only=True)
    status_display = serializers.CharField(source="get_status_display", read_only=True)
    intervention_type_name = serializers.CharField(source="intervention_type.name", read_only=True)
    supplier_name = serializers.CharField(source="supplier.name", read_only=True, default=None)
    driver_name = serializers.CharField(source="driver.full_name", read_only=True, default=None)

    class Meta:
        model = Service
        fields = [
            "id", "description",
            "vehicle", "vehicle_plate",
            "intervention_type", "intervention_type_name",
            "date", "supplier", "supplier_name",
            "cost", "currency", "notes",
            "driver", "driver_name",
            "status", "status_display",
            "odometer_reading",
            "created_at", "updated_at",
        ]


# ---------------------------------------------------------------------------
# ServiceAttachment
# ---------------------------------------------------------------------------
class ServiceAttachmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAttachment
        fields = ["id", "service", "file_name", "description"]


class ServiceAttachmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAttachment
        fields = [
            "id", "service", "file", "file_name",
            "description", "created_at", "updated_at",
        ]


# ---------------------------------------------------------------------------
# Contract
# ---------------------------------------------------------------------------
class ContractListSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.CharField(source="vehicle.license_plate", read_only=True)
    status_display = serializers.CharField(source="get_status_display", read_only=True)
    intervention_type_name = serializers.CharField(source="intervention_type.name", read_only=True)

    class Meta:
        model = Contract
        fields = [
            "id", "name", "reference",
            "vehicle", "vehicle_plate",
            "intervention_type", "intervention_type_name",
            "start_date", "end_date",
            "status", "status_display",
        ]


class ContractDetailSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.CharField(source="vehicle.license_plate", read_only=True)
    status_display = serializers.CharField(source="get_status_display", read_only=True)
    intervention_type_name = serializers.CharField(source="intervention_type.name", read_only=True)
    supplier_name = serializers.CharField(source="supplier.name", read_only=True, default=None)
    driver_name = serializers.CharField(source="driver.full_name", read_only=True, default=None)
    billing_period_name = serializers.CharField(source="billing_period.name", read_only=True, default=None)
    is_expired = serializers.BooleanField(read_only=True)

    class Meta:
        model = Contract
        fields = [
            "id", "name", "reference",
            "intervention_type", "intervention_type_name",
            "included_services",
            "supplier", "supplier_name",
            "start_date", "end_date", "creation_date",
            "responsible",
            "vehicle", "vehicle_plate",
            "driver", "driver_name",
            "activation_cost",
            "billing_period", "billing_period_name",
            "currency",
            "status", "status_display",
            "terms", "is_expired",
            "created_at", "updated_at",
        ]


# ---------------------------------------------------------------------------
# RecurringCost
# ---------------------------------------------------------------------------
class RecurringCostListSerializer(serializers.ModelSerializer):
    period_name = serializers.CharField(source="period.name", read_only=True)

    class Meta:
        model = RecurringCost
        fields = ["id", "contract", "description", "amount", "currency", "period", "period_name"]


class RecurringCostDetailSerializer(serializers.ModelSerializer):
    period_name = serializers.CharField(source="period.name", read_only=True)

    class Meta:
        model = RecurringCost
        fields = [
            "id", "contract", "description",
            "amount", "currency",
            "period", "period_name",
            "created_at", "updated_at",
        ]
