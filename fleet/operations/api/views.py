from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Service, ServiceAttachment, Contract, RecurringCost
from ..serializers import (
    ServiceListSerializer, ServiceDetailSerializer,
    ServiceAttachmentListSerializer, ServiceAttachmentDetailSerializer,
    ContractListSerializer, ContractDetailSerializer,
    RecurringCostListSerializer, RecurringCostDetailSerializer,
)
from .. import services, selectors


class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_services()

    def get_serializer_class(self):
        if self.action == "list":
            return ServiceListSerializer
        return ServiceDetailSerializer

    def perform_create(self, serializer):
        services.create_service(
            data=serializer.validated_data,
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_service(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_service(instance=instance)

    @action(detail=True, methods=["post"])
    def change_status(self, request, pk=None):
        service = self.get_object()
        new_status = request.data.get("status")
        if new_status not in Service.Status.values:
            return Response({"detail": "Invalid status."}, status=status.HTTP_400_BAD_REQUEST)
        updated = services.change_service_status(instance=service, status=new_status)
        return Response(ServiceDetailSerializer(updated).data)

    @action(detail=True, methods=["get"])
    def attachments(self, request, pk=None):
        service = self.get_object()
        qs = selectors.get_attachments_for_service(service_id=service.id)
        serializer = ServiceAttachmentListSerializer(qs, many=True)
        return Response(serializer.data)


class ServiceAttachmentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ServiceAttachment.objects.select_related("service").all()

    def get_serializer_class(self):
        if self.action == "list":
            return ServiceAttachmentListSerializer
        return ServiceAttachmentDetailSerializer

    def perform_create(self, serializer):
        services.create_service_attachment(
            service_id=serializer.validated_data["service"].id,
            file=serializer.validated_data["file"],
            file_name=serializer.validated_data.get("file_name", ""),
            description=serializer.validated_data.get("description", ""),
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_service_attachment(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_service_attachment(instance=instance)


class ContractViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return selectors.get_all_contracts()

    def get_serializer_class(self):
        if self.action == "list":
            return ContractListSerializer
        return ContractDetailSerializer

    def perform_create(self, serializer):
        services.create_contract(
            data=serializer.validated_data,
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_contract(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_contract(instance=instance)

    @action(detail=True, methods=["post"])
    def activate(self, request, pk=None):
        contract = self.get_object()
        updated = services.activate_contract(instance=contract)
        return Response(ContractDetailSerializer(updated).data)

    @action(detail=True, methods=["post"])
    def cancel(self, request, pk=None):
        contract = self.get_object()
        updated = services.cancel_contract(instance=contract)
        return Response(ContractDetailSerializer(updated).data)

    @action(detail=True, methods=["post"])
    def expire(self, request, pk=None):
        contract = self.get_object()
        updated = services.expire_contract(instance=contract)
        return Response(ContractDetailSerializer(updated).data)

    @action(detail=True, methods=["get"])
    def recurring_costs(self, request, pk=None):
        contract = self.get_object()
        qs = selectors.get_recurring_costs_for_contract(contract_id=contract.id)
        serializer = RecurringCostListSerializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def expiring_soon(self, request):
        """Contracts expiring within the next N days (default 30)."""
        days = int(request.query_params.get("days", 30))
        qs = selectors.get_expiring_contracts(days=days)
        serializer = ContractListSerializer(qs, many=True)
        return Response(serializer.data)


class RecurringCostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RecurringCost.objects.select_related("period", "contract").all()

    def get_serializer_class(self):
        if self.action == "list":
            return RecurringCostListSerializer
        return RecurringCostDetailSerializer

    def perform_create(self, serializer):
        services.create_recurring_cost(
            contract_id=serializer.validated_data["contract"].id,
            description=serializer.validated_data["description"],
            amount=serializer.validated_data["amount"],
            currency=serializer.validated_data.get("currency", "XAF"),
            period_id=serializer.validated_data["period"].id,
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        services.update_recurring_cost(
            instance=self.get_object(),
            data=serializer.validated_data,
        )

    def perform_destroy(self, instance):
        services.delete_recurring_cost(instance=instance)
