import datetime
from django.db.models import QuerySet
from .models import Service, ServiceAttachment, Contract, RecurringCost


# ---------------------------------------------------------------------------
# Service
# ---------------------------------------------------------------------------
def get_all_services() -> QuerySet:
    return Service.objects.select_related(
        "vehicle", "intervention_type", "supplier", "driver"
    ).all()


def get_services_for_vehicle(*, vehicle_id) -> QuerySet:
    return Service.objects.select_related(
        "intervention_type", "supplier", "driver"
    ).filter(vehicle_id=vehicle_id)


def get_services_by_status(*, status: str) -> QuerySet:
    return Service.objects.select_related(
        "vehicle", "intervention_type", "supplier", "driver"
    ).filter(status=status)


def get_services_by_supplier(*, supplier_id) -> QuerySet:
    return Service.objects.select_related(
        "vehicle", "intervention_type", "driver"
    ).filter(supplier_id=supplier_id)


def get_service_by_id(*, service_id) -> Service:
    return Service.objects.select_related(
        "vehicle", "intervention_type", "supplier", "driver"
    ).get(id=service_id)


# ---------------------------------------------------------------------------
# ServiceAttachment
# ---------------------------------------------------------------------------
def get_attachments_for_service(*, service_id) -> QuerySet:
    return ServiceAttachment.objects.filter(service_id=service_id)


def get_service_attachment_by_id(*, attachment_id) -> ServiceAttachment:
    return ServiceAttachment.objects.select_related("service").get(id=attachment_id)


# ---------------------------------------------------------------------------
# Contract
# ---------------------------------------------------------------------------
def get_all_contracts() -> QuerySet:
    return Contract.objects.select_related(
        "vehicle", "intervention_type", "supplier", "driver", "billing_period"
    ).all()


def get_contracts_for_vehicle(*, vehicle_id) -> QuerySet:
    return Contract.objects.select_related(
        "intervention_type", "supplier", "driver", "billing_period"
    ).filter(vehicle_id=vehicle_id)


def get_contracts_by_status(*, status: str) -> QuerySet:
    return Contract.objects.select_related(
        "vehicle", "intervention_type", "supplier", "driver", "billing_period"
    ).filter(status=status)


def get_active_contracts() -> QuerySet:
    return get_contracts_by_status(status=Contract.Status.ACTIVE)


def get_expiring_contracts(*, days: int = 30) -> QuerySet:
    threshold = datetime.date.today() + datetime.timedelta(days=days)
    return Contract.objects.select_related(
        "vehicle", "intervention_type", "supplier"
    ).filter(
        end_date__lte=threshold,
        end_date__gte=datetime.date.today(),
        status=Contract.Status.ACTIVE,
    )


def get_contract_by_id(*, contract_id) -> Contract:
    return Contract.objects.select_related(
        "vehicle", "intervention_type", "supplier",
        "driver", "billing_period", "responsible",
    ).prefetch_related("included_services", "recurring_costs").get(id=contract_id)


def get_contracts_by_supplier(*, supplier_id) -> QuerySet:
    return Contract.objects.select_related(
        "vehicle", "intervention_type", "billing_period"
    ).filter(supplier_id=supplier_id)


# ---------------------------------------------------------------------------
# RecurringCost
# ---------------------------------------------------------------------------
def get_recurring_costs_for_contract(*, contract_id) -> QuerySet:
    return RecurringCost.objects.select_related("period").filter(contract_id=contract_id)


def get_recurring_cost_by_id(*, recurring_cost_id) -> RecurringCost:
    return RecurringCost.objects.select_related("period", "contract").get(id=recurring_cost_id)
