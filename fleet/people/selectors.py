from django.db.models import QuerySet
from .models import Driver, Supplier, Manufacturer


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
def get_all_drivers() -> QuerySet:
    return Driver.objects.select_related("user").all()


def get_active_drivers() -> QuerySet:
    return Driver.objects.select_related("user").filter(is_active=True)


def get_driver_by_id(*, driver_id) -> Driver:
    return Driver.objects.select_related("user").get(id=driver_id)


def search_drivers(*, query: str) -> QuerySet:
    from django.db.models import Q
    return Driver.objects.filter(
        Q(first_name__icontains=query) |
        Q(last_name__icontains=query) |
        Q(employee_id__icontains=query)
    )


# ---------------------------------------------------------------------------
# Supplier
# ---------------------------------------------------------------------------
def get_all_suppliers() -> QuerySet:
    return Supplier.objects.all()


def get_active_suppliers() -> QuerySet:
    return Supplier.objects.filter(is_active=True)


def get_supplier_by_id(*, supplier_id) -> Supplier:
    return Supplier.objects.get(id=supplier_id)


def search_suppliers(*, query: str) -> QuerySet:
    from django.db.models import Q
    return Supplier.objects.filter(
        Q(name__icontains=query) | Q(code__icontains=query) | Q(city__icontains=query)
    )


# ---------------------------------------------------------------------------
# Manufacturer
# ---------------------------------------------------------------------------
def get_all_manufacturers() -> QuerySet:
    return Manufacturer.objects.all()


def get_manufacturer_by_id(*, manufacturer_id) -> Manufacturer:
    return Manufacturer.objects.get(id=manufacturer_id)


def search_manufacturers(*, query: str) -> QuerySet:
    return Manufacturer.objects.filter(name__icontains=query)
