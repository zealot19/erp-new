from .models import Service, ServiceAttachment, Contract, RecurringCost


# ---------------------------------------------------------------------------
# Service
# ---------------------------------------------------------------------------
def create_service(*, data: dict, created_by=None) -> Service:
    return Service.objects.create(**data, created_by=created_by)


def update_service(*, instance: Service, data: dict) -> Service:
    allowed = [
        "description", "vehicle_id", "intervention_type_id", "date",
        "supplier_id", "cost", "currency", "notes",
        "driver_id", "status", "odometer_reading",
    ]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    return instance


def delete_service(*, instance: Service) -> None:
    instance.delete()


def change_service_status(*, instance: Service, status: str) -> Service:
    instance.status = status
    instance.save(update_fields=["status", "updated_at"])
    return instance


# ---------------------------------------------------------------------------
# ServiceAttachment
# ---------------------------------------------------------------------------
def create_service_attachment(*, service_id, file, file_name: str = "", description: str = "", created_by=None) -> ServiceAttachment:
    return ServiceAttachment.objects.create(
        service_id=service_id,
        file=file,
        file_name=file_name,
        description=description,
        created_by=created_by,
    )


def update_service_attachment(*, instance: ServiceAttachment, data: dict) -> ServiceAttachment:
    allowed = ["file", "file_name", "description"]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    return instance


def delete_service_attachment(*, instance: ServiceAttachment) -> None:
    instance.delete()


# ---------------------------------------------------------------------------
# Contract
# ---------------------------------------------------------------------------
def create_contract(*, data: dict, created_by=None) -> Contract:
    included_services = data.pop("included_services", [])
    instance = Contract.objects.create(**data, created_by=created_by)
    if included_services:
        instance.included_services.set(included_services)
    return instance


def update_contract(*, instance: Contract, data: dict) -> Contract:
    included_services = data.pop("included_services", None)
    allowed = [
        "name", "reference", "intervention_type_id",
        "supplier_id", "start_date", "end_date", "creation_date",
        "responsible_id", "vehicle_id", "driver_id",
        "activation_cost", "billing_period_id", "currency",
        "status", "terms",
    ]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    if included_services is not None:
        instance.included_services.set(included_services)
    return instance


def delete_contract(*, instance: Contract) -> None:
    instance.delete()


def change_contract_status(*, instance: Contract, status: str) -> Contract:
    instance.status = status
    instance.save(update_fields=["status", "updated_at"])
    return instance


def activate_contract(*, instance: Contract) -> Contract:
    return change_contract_status(instance=instance, status=Contract.Status.ACTIVE)


def cancel_contract(*, instance: Contract) -> Contract:
    return change_contract_status(instance=instance, status=Contract.Status.CANCELLED)


def expire_contract(*, instance: Contract) -> Contract:
    return change_contract_status(instance=instance, status=Contract.Status.EXPIRED)


# ---------------------------------------------------------------------------
# RecurringCost
# ---------------------------------------------------------------------------
def create_recurring_cost(*, contract_id, description: str, amount, currency: str = "XAF", period_id=None, created_by=None) -> RecurringCost:
    return RecurringCost.objects.create(
        contract_id=contract_id,
        description=description,
        amount=amount,
        currency=currency,
        period_id=period_id,
        created_by=created_by,
    )


def update_recurring_cost(*, instance: RecurringCost, data: dict) -> RecurringCost:
    allowed = ["description", "amount", "currency", "period_id"]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    return instance


def delete_recurring_cost(*, instance: RecurringCost) -> None:
    instance.delete()
