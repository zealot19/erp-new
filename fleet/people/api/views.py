from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Driver, Supplier, Manufacturer
from ..serializers import (
    DriverListSerializer, DriverDetailSerializer,
    SupplierListSerializer, SupplierDetailSerializer,
    ManufacturerListSerializer, ManufacturerDetailSerializer,
)
from .. import services, selectors


class DriverViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_drivers()

    def get_serializer_class(self):
        if self.action == "list":
            return DriverListSerializer
        return DriverDetailSerializer

    def perform_create(self, serializer):
        services.create_driver(
            data=serializer.validated_data,
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_driver(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_driver(instance=instance)

    @action(detail=True, methods=["post"])
    def activate(self, request, pk=None):
        driver = self.get_object()
        services.activate_driver(instance=driver)
        return Response(DriverDetailSerializer(driver).data)

    @action(detail=True, methods=["post"])
    def deactivate(self, request, pk=None):
        driver = self.get_object()
        services.deactivate_driver(instance=driver)
        return Response(DriverDetailSerializer(driver).data)


class SupplierViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_suppliers()

    def get_serializer_class(self):
        if self.action == "list":
            return SupplierListSerializer
        return SupplierDetailSerializer

    def perform_create(self, serializer):
        services.create_supplier(
            data=serializer.validated_data,
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_supplier(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_supplier(instance=instance)

    @action(detail=True, methods=["post"])
    def deactivate(self, request, pk=None):
        supplier = self.get_object()
        services.deactivate_supplier(instance=supplier)
        return Response(SupplierDetailSerializer(supplier).data)


class ManufacturerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_manufacturers()

    def get_serializer_class(self):
        if self.action == "list":
            return ManufacturerListSerializer
        return ManufacturerDetailSerializer

    def perform_create(self, serializer):
        services.create_manufacturer(
            name=serializer.validated_data["name"],
            country=serializer.validated_data.get("country", ""),
            logo=serializer.validated_data.get("logo"),
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_manufacturer(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_manufacturer(instance=instance)
