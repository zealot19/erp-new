from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import (
    VehicleCategory, VehicleType, FuelType, Transmission, TractionType,
    UnitCategory, Unit, ActivitySector, Period, InterventionType,
    DocumentType, Tag,
)
from ..serializers import (
    VehicleCategoryListSerializer, VehicleCategoryDetailSerializer,
    VehicleTypeListSerializer, VehicleTypeDetailSerializer,
    FuelTypeListSerializer, FuelTypeDetailSerializer,
    TransmissionListSerializer, TransmissionDetailSerializer,
    TractionTypeListSerializer, TractionTypeDetailSerializer,
    UnitCategoryListSerializer, UnitCategoryDetailSerializer,
    UnitListSerializer, UnitDetailSerializer,
    ActivitySectorListSerializer, ActivitySectorDetailSerializer,
    PeriodListSerializer, PeriodDetailSerializer,
    InterventionTypeListSerializer, InterventionTypeDetailSerializer,
    DocumentTypeListSerializer, DocumentTypeDetailSerializer,
    TagListSerializer, TagDetailSerializer,
)
from .. import services, selectors


class VehicleCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_vehicle_categories()

    def get_serializer_class(self):
        if self.action == "list":
            return VehicleCategoryListSerializer
        return VehicleCategoryDetailSerializer

    def perform_create(self, serializer):
        services.create_vehicle_category(
            name=serializer.validated_data["name"],
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_vehicle_category(
            instance=self.get_object(),
            name=serializer.validated_data["name"],
        )

    def perform_destroy(self, instance):
        services.delete_vehicle_category(instance=instance)


class VehicleTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_vehicle_types()

    def get_serializer_class(self):
        if self.action == "list":
            return VehicleTypeListSerializer
        return VehicleTypeDetailSerializer

    def perform_create(self, serializer):
        services.create_vehicle_type(
            name=serializer.validated_data["name"],
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_vehicle_type(
            instance=self.get_object(),
            name=serializer.validated_data["name"],
        )

    def perform_destroy(self, instance):
        services.delete_vehicle_type(instance=instance)


class FuelTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_fuel_types()

    def get_serializer_class(self):
        if self.action == "list":
            return FuelTypeListSerializer
        return FuelTypeDetailSerializer

    def perform_create(self, serializer):
        services.create_fuel_type(
            name=serializer.validated_data["name"],
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_fuel_type(
            instance=self.get_object(),
            name=serializer.validated_data["name"],
        )

    def perform_destroy(self, instance):
        services.delete_fuel_type(instance=instance)


class TransmissionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_transmissions()

    def get_serializer_class(self):
        if self.action == "list":
            return TransmissionListSerializer
        return TransmissionDetailSerializer

    def perform_create(self, serializer):
        services.create_transmission(
            name=serializer.validated_data["name"],
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_transmission(
            instance=self.get_object(),
            name=serializer.validated_data["name"],
        )

    def perform_destroy(self, instance):
        services.delete_transmission(instance=instance)


class TractionTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_traction_types()

    def get_serializer_class(self):
        if self.action == "list":
            return TractionTypeListSerializer
        return TractionTypeDetailSerializer

    def perform_create(self, serializer):
        services.create_traction_type(
            name=serializer.validated_data["name"],
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_traction_type(
            instance=self.get_object(),
            name=serializer.validated_data["name"],
        )

    def perform_destroy(self, instance):
        services.delete_traction_type(instance=instance)


class UnitCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_unit_categories()

    def get_serializer_class(self):
        if self.action == "list":
            return UnitCategoryListSerializer
        return UnitCategoryDetailSerializer

    def perform_create(self, serializer):
        services.create_unit_category(
            name=serializer.validated_data["name"],
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_unit_category(
            instance=self.get_object(),
            name=serializer.validated_data["name"],
        )

    def perform_destroy(self, instance):
        services.delete_unit_category(instance=instance)

    @action(detail=True, methods=["get"])
    def units(self, request, pk=None):
        """List all units belonging to this category."""
        category = self.get_object()
        qs = selectors.get_units_by_category(category_id=category.id)
        serializer = UnitListSerializer(qs, many=True)
        return Response(serializer.data)


class UnitViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_units()

    def get_serializer_class(self):
        if self.action == "list":
            return UnitListSerializer
        return UnitDetailSerializer

    def perform_create(self, serializer):
        services.create_unit(
            category_id=serializer.validated_data["category"].id,
            code=serializer.validated_data["code"],
            name=serializer.validated_data["name"],
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_unit(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_unit(instance=instance)


class ActivitySectorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_activity_sectors()

    def get_serializer_class(self):
        if self.action == "list":
            return ActivitySectorListSerializer
        return ActivitySectorDetailSerializer

    def perform_create(self, serializer):
        services.create_activity_sector(
            code=serializer.validated_data["code"],
            name=serializer.validated_data["name"],
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_activity_sector(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_activity_sector(instance=instance)


class PeriodViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_periods()

    def get_serializer_class(self):
        if self.action == "list":
            return PeriodListSerializer
        return PeriodDetailSerializer

    def perform_create(self, serializer):
        services.create_period(
            name=serializer.validated_data["name"],
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_period(
            instance=self.get_object(),
            name=serializer.validated_data["name"],
        )

    def perform_destroy(self, instance):
        services.delete_period(instance=instance)


class InterventionTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_intervention_types()

    def get_serializer_class(self):
        if self.action == "list":
            return InterventionTypeListSerializer
        return InterventionTypeDetailSerializer

    def perform_create(self, serializer):
        services.create_intervention_type(
            name=serializer.validated_data["name"],
            category=serializer.validated_data["category"],
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_intervention_type(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_intervention_type(instance=instance)


class DocumentTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_document_types()

    def get_serializer_class(self):
        if self.action == "list":
            return DocumentTypeListSerializer
        return DocumentTypeDetailSerializer

    def perform_create(self, serializer):
        services.create_document_type(
            code=serializer.validated_data["code"],
            label=serializer.validated_data["label"],
            requires_expiration=serializer.validated_data.get("requires_expiration", True),
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_document_type(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_document_type(instance=instance)


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_tags()

    def get_serializer_class(self):
        if self.action == "list":
            return TagListSerializer
        return TagDetailSerializer

    def perform_create(self, serializer):
        services.create_tag(
            name=serializer.validated_data["name"],
            color=serializer.validated_data.get("color", ""),
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_tag(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_tag(instance=instance)
