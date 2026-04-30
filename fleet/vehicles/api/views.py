from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import VehicleModel, Parking, Vehicle, OdometerReading, VehicleDocument, VehicleLayout, Seat
from ..serializers import (
    VehicleModelListSerializer, VehicleModelDetailSerializer,
    ParkingListSerializer, ParkingDetailSerializer,
    VehicleListSerializer, VehicleDetailSerializer,
    OdometerReadingListSerializer, OdometerReadingDetailSerializer,
    VehicleDocumentListSerializer, VehicleDocumentDetailSerializer,
    VehicleLayoutListSerializer, VehicleLayoutDetailSerializer,
    SeatListSerializer, SeatDetailSerializer,
)
from .. import services, selectors


class VehicleModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_vehicle_models()

    def get_serializer_class(self):
        if self.action == "list":
            return VehicleModelListSerializer
        return VehicleModelDetailSerializer

    def perform_create(self, serializer):
        services.create_vehicle_model(
            data=serializer.validated_data,
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_vehicle_model(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_vehicle_model(instance=instance)


class ParkingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_parkings()

    def get_serializer_class(self):
        if self.action == "list":
            return ParkingListSerializer
        return ParkingDetailSerializer

    def perform_create(self, serializer):
        services.create_parking(
            name=serializer.validated_data["name"],
            location=serializer.validated_data.get("location", ""),
            notes=serializer.validated_data.get("notes", ""),
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_parking(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_parking(instance=instance)

    @action(detail=True, methods=["get"])
    def vehicles(self, request, pk=None):
        """List all vehicles currently parked here."""
        parking = self.get_object()
        qs = selectors.get_vehicles_by_parking(parking_id=parking.id)
        serializer = VehicleListSerializer(qs, many=True)
        return Response(serializer.data)


class VehicleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_vehicles()

    def get_serializer_class(self):
        if self.action == "list":
            return VehicleListSerializer
        return VehicleDetailSerializer

    def perform_create(self, serializer):
        services.create_vehicle(
            data=serializer.validated_data,
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_vehicle(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_vehicle(instance=instance)

    @action(detail=True, methods=["post"])
    def change_state(self, request, pk=None):
        vehicle = self.get_object()
        state = request.data.get("state")
        if state not in Vehicle.State.values:
            return Response({"detail": "Invalid state."}, status=status.HTTP_400_BAD_REQUEST)
        updated = services.change_vehicle_state(instance=vehicle, state=state)
        return Response(VehicleDetailSerializer(updated).data)

    @action(detail=True, methods=["post"])
    def assign_driver(self, request, pk=None):
        vehicle = self.get_object()
        driver_id = request.data.get("driver_id")
        updated = services.assign_driver(instance=vehicle, driver_id=driver_id)
        return Response(VehicleDetailSerializer(updated).data)

    @action(detail=True, methods=["post"])
    def assign_parking(self, request, pk=None):
        vehicle = self.get_object()
        parking_id = request.data.get("parking_id")
        updated = services.assign_parking(instance=vehicle, parking_id=parking_id)
        return Response(VehicleDetailSerializer(updated).data)

    @action(detail=True, methods=["get"])
    def odometer_readings(self, request, pk=None):
        vehicle = self.get_object()
        qs = selectors.get_odometer_readings_for_vehicle(vehicle_id=vehicle.id)
        serializer = OdometerReadingListSerializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def documents(self, request, pk=None):
        vehicle = self.get_object()
        qs = selectors.get_documents_for_vehicle(vehicle_id=vehicle.id)
        serializer = VehicleDocumentListSerializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def layouts(self, request, pk=None):
        vehicle = self.get_object()
        qs = selectors.get_layouts_for_vehicle(vehicle_id=vehicle.id)
        serializer = VehicleLayoutListSerializer(qs, many=True)
        return Response(serializer.data)


class OdometerReadingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return OdometerReading.objects.select_related("unit", "vehicle").all()

    def get_serializer_class(self):
        if self.action == "list":
            return OdometerReadingListSerializer
        return OdometerReadingDetailSerializer

    def perform_create(self, serializer):
        services.create_odometer_reading(
            data=serializer.validated_data,
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_odometer_reading(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_odometer_reading(instance=instance)


class VehicleDocumentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return VehicleDocument.objects.select_related("document_type", "vehicle").all()

    def get_serializer_class(self):
        if self.action == "list":
            return VehicleDocumentListSerializer
        return VehicleDocumentDetailSerializer

    def perform_create(self, serializer):
        services.create_vehicle_document(
            data=serializer.validated_data,
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_vehicle_document(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_vehicle_document(instance=instance)

    @action(detail=False, methods=["get"])
    def expiring_soon(self, request):
        """Documents expiring within the next 30 days."""
        days = int(request.query_params.get("days", 30))
        qs = selectors.get_expiring_documents(days=days)
        serializer = VehicleDocumentListSerializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def expired(self, request):
        """Documents that have already expired."""
        qs = selectors.get_expired_documents()
        serializer = VehicleDocumentListSerializer(qs, many=True)
        return Response(serializer.data)


class VehicleLayoutViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return VehicleLayout.objects.select_related("vehicle").all()

    def get_serializer_class(self):
        if self.action == "list":
            return VehicleLayoutListSerializer
        return VehicleLayoutDetailSerializer

    def perform_create(self, serializer):
        services.create_vehicle_layout(
            vehicle_id=serializer.validated_data["vehicle"].id,
            name=serializer.validated_data["name"],
            total_seats=serializer.validated_data["total_seats"],
            is_active=serializer.validated_data.get("is_active", False),
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_vehicle_layout(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_vehicle_layout(instance=instance)

    @action(detail=True, methods=["post"])
    def activate(self, request, pk=None):
        """Set this layout as the active layout for its vehicle."""
        layout = self.get_object()
        updated = services.activate_layout(instance=layout)
        return Response(VehicleLayoutDetailSerializer(updated).data)

    @action(detail=True, methods=["get"])
    def seats(self, request, pk=None):
        """List all seats in this layout."""
        layout = self.get_object()
        qs = selectors.get_seats_for_layout(layout_id=layout.id)
        serializer = SeatListSerializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def available_seats(self, request, pk=None):
        """List only available seats in this layout."""
        layout = self.get_object()
        qs = selectors.get_available_seats_for_layout(layout_id=layout.id)
        serializer = SeatListSerializer(qs, many=True)
        return Response(serializer.data)


class SeatViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Seat.objects.select_related("layout").all()

    def get_serializer_class(self):
        if self.action == "list":
            return SeatListSerializer
        return SeatDetailSerializer

    def perform_create(self, serializer):
        services.create_seat(
            data=serializer.validated_data,
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_seat(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_seat(instance=instance)
