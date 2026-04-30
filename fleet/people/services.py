from .models import Driver, Supplier, Manufacturer


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
def create_driver(*, data: dict, created_by=None) -> Driver:
    return Driver.objects.create(**data, created_by=created_by)


def update_driver(*, instance: Driver, data: dict) -> Driver:
    allowed = [
        "user_id", "employee_id", "first_name", "last_name",
        "phone", "email", "license_number", "license_expiry",
        "license_category", "is_active",
    ]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    return instance


def delete_driver(*, instance: Driver) -> None:
    instance.delete()


def deactivate_driver(*, instance: Driver) -> Driver:
    instance.is_active = False
    instance.save(update_fields=["is_active", "updated_at"])
    return instance


def activate_driver(*, instance: Driver) -> Driver:
    instance.is_active = True
    instance.save(update_fields=["is_active", "updated_at"])
    return instance


# ---------------------------------------------------------------------------
# Supplier
# ---------------------------------------------------------------------------
def create_supplier(*, data: dict, created_by=None) -> Supplier:
    return Supplier.objects.create(**data, created_by=created_by)


def update_supplier(*, instance: Supplier, data: dict) -> Supplier:
    allowed = [
        "name", "code", "tax_id", "address", "city", "country",
        "phone", "email", "website", "contact_person", "notes", "is_active",
    ]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    return instance


def delete_supplier(*, instance: Supplier) -> None:
    instance.delete()


def deactivate_supplier(*, instance: Supplier) -> Supplier:
    instance.is_active = False
    instance.save(update_fields=["is_active", "updated_at"])
    return instance


# ---------------------------------------------------------------------------
# Manufacturer
# ---------------------------------------------------------------------------
def create_manufacturer(*, name: str, country: str = "", logo=None, created_by=None) -> Manufacturer:
    return Manufacturer.objects.create(name=name, country=country, logo=logo, created_by=created_by)


def update_manufacturer(*, instance: Manufacturer, data: dict) -> Manufacturer:
    allowed = ["name", "country", "logo"]
    for field in allowed:
        if field in data:
            setattr(instance, field, data[field])
    instance.save(update_fields=[f for f in allowed if f in data] + ["updated_at"])
    return instance


def delete_manufacturer(*, instance: Manufacturer) -> None:
    instance.delete()
