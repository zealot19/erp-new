from django.db import models
import uuid
from core.models import BaseModel

class VehicleCategory(BaseModel):
    """
    High-level grouping for vehicles.
    Examples: Utilitaire, Berline, SUV, Bus, Minibus.
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "vehicle categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class VehicleType(BaseModel):
    """
    Physical type of vehicle.
    Examples: Voiture, Moto, Vélo, Camion, Bus.
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class FuelType(BaseModel):
    """
    Fuel / energy source.
    Examples: Essence, Diesel, Électrique, Hybride, GPL.
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Transmission(BaseModel):
    """
    Gearbox type.
    Examples: Manuelle, Automatique, Semi-automatique.
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class TractionType(BaseModel):
    """
    Drive system.
    Examples: Traction avant, Propulsion, 4x4, AWD.
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class UnitCategory(BaseModel):
    """
    Groups related measurement units.
    Examples: Puissance, Distance, Émission, Volume.
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "unit categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Unit(BaseModel):
    """
    Measurement unit belonging to a category.
    Examples: (Puissance) ch, kW, hp — (Distance) km, mi — (Émission) g/km.
    """
    category = models.ForeignKey(UnitCategory, on_delete=models.CASCADE, related_name="units")
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["category", "code"]

    def __str__(self):
        return f"{self.code} — {self.name}"


class ActivitySector(BaseModel):
    """
    Business sector the fleet operates in.
    Examples: Transport urbain, Logistique, Mining, Agriculture.
    """
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} — {self.name}"


class Period(BaseModel):
    """
    Billing or recurrence period.
    Examples: Mensuel, Trimestriel, Annuel, Hebdomadaire.
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class InterventionType(BaseModel):
    """
    Type of maintenance, repair, or contract intervention.
    The category indicates whether this applies to services, contracts, or both.
    """

    class Category(models.TextChoices):
        CONTRACT = "CONTRACT", "Contrat"
        SERVICE = "SERVICE", "Service"
        BOTH = "BOTH", "Contrat et Service"

    name = models.CharField(max_length=255)
    category = models.CharField(
        max_length=10, choices=Category.choices, default=Category.BOTH,
        help_text="Whether this intervention is linked to a contract, a service, or both."
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class DocumentType(BaseModel):
    """
    Administrative document type (configurable, not hardcoded).
    Examples: Assurance, Carte grise, Visite technique, Vignette.
    """
    code = models.CharField(max_length=20, unique=True)
    label = models.CharField(max_length=255)
    requires_expiration = models.BooleanField(
        default=True,
        help_text="Whether documents of this type have an expiration date."
    )

    class Meta:
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} — {self.label}"


class Tag(BaseModel):
    """
    Free-form label / étiquette that can be attached to vehicles.
    Examples: Pool, Direction, Chantier, Location.
    """
    name = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=7, blank=True, help_text="Hex color code, e.g. #FF5733")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
