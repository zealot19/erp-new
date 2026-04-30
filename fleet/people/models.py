from django.db import models
from core.models import BaseModel


class Driver(BaseModel):
    """
    A person authorised to drive fleet vehicles.
    Can be an employee or an external contractor.
    """
    user = models.OneToOneField(
        "auth.User", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="driver_profile"
    )
    employee_id = models.CharField(max_length=30, blank=True, help_text="Internal employee number")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    license_number = models.CharField(max_length=50, blank=True)
    license_expiry = models.DateField(null=True, blank=True)
    license_category = models.CharField(
        max_length=20, blank=True,
        help_text="Driving license category. e.g. B, C, D, CE"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Supplier(BaseModel):
    """
    External company providing services, parts, fuel, contracts, or vehicles.
    Referred to as 'Fournisseur' or 'Société associée' in the spec.
    """
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20, unique=True)
    tax_id = models.CharField(max_length=50, blank=True, verbose_name="NIU / Tax ID")
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=2, default="CM")
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    contact_person = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.code} — {self.name}"


class Manufacturer(BaseModel):
    """
    Vehicle manufacturer / brand.
    Examples: Toyota, Mercedes-Benz, Volvo, Renault, Hyundai.
    """
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=2, blank=True, help_text="Country of origin (ISO 3166-1)")
    logo = models.ImageField(upload_to="manufacturers/logos/", null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
