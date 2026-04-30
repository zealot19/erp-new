import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import BaseModel


class VehicleModel(BaseModel):
    """
    Manufacturer's model specification (the "blueprint").
    Example: Toyota Hilux 2024, Volvo B8R 2023.
    Multiple fleet vehicles can reference the same model.
    """
    image = models.ImageField(upload_to="vehicle_models/", null=True, blank=True)
    vehicle_type = models.ForeignKey(
        "config.VehicleType", on_delete=models.PROTECT, related_name="vehicle_models",
        help_text="Physical type: Voiture, Bus, Camion, Moto, etc."
    )
    manufacturer = models.ForeignKey(
        "people.Manufacturer", on_delete=models.PROTECT, related_name="vehicle_models"
    )
    name = models.CharField(max_length=255, help_text="Model name. e.g. Hilux, Corolla, B8R")
    model_year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1970), MaxValueValidator(datetime.date.today().year + 1)],
        help_text="Year of the model (1970 to current year)"
    )
    seats = models.PositiveSmallIntegerField(
        null=True, blank=True, help_text="Number of seats"
    )
    doors = models.PositiveSmallIntegerField(
        null=True, blank=True, help_text="Number of doors"
    )
    color = models.CharField(max_length=50, blank=True)
    has_tow_hitch = models.BooleanField(
        default=False,
        help_text="Whether the model has a tow hitch (attelage remorque)"
    )

    fuel_type = models.ForeignKey(
        "config.FuelType", on_delete=models.PROTECT, related_name="vehicle_models"
    )
    transmission = models.ForeignKey(
        "config.Transmission", on_delete=models.PROTECT, related_name="vehicle_models"
    )
    traction_type = models.ForeignKey(
        "config.TractionType", on_delete=models.PROTECT, related_name="vehicle_models"
    )

    power = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        help_text="Engine power value"
    )
    power_unit = models.ForeignKey(
        "config.Unit", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="vehicle_model_power",
        help_text="Unit for power. e.g. ch, kW, hp"
    )
    range_value = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        help_text="Range / plage (especially for electric vehicles)"
    )
    range_unit = models.ForeignKey(
        "config.Unit", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="vehicle_model_range",
        help_text="Unit for range. e.g. km, mi"
    )

    co2_emission = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        help_text="CO2 emission value"
    )
    emission_unit = models.ForeignKey(
        "config.Unit", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="vehicle_model_emission",
        help_text="Unit for CO2 emission. e.g. g/km"
    )
    emission_standard = models.CharField(
        max_length=50, blank=True,
        help_text="Emission standard. e.g. Euro 6, Euro 5, Tier 4"
    )

    suppliers = models.ManyToManyField(
        "people.Supplier", blank=True, related_name="vehicle_models",
        help_text="Suppliers/dealers that can provide this model"
    )

    class Meta:
        unique_together = ("manufacturer", "name", "model_year")
        ordering = ["manufacturer", "name", "-model_year"]

    def __str__(self):
        return f"{self.manufacturer.name} {self.name} ({self.model_year})"



class Parking(BaseModel):
    """
    Physical location where vehicles are parked or stored.
    Examples: Parking Siège Douala, Dépôt Yaoundé, Atelier Kribi.
    """
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, help_text="Address or GPS coordinates")
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Vehicle(BaseModel):
    """
    A physical vehicle in the fleet.
    Tracks registration, assignment, fiscal info, state, and lifecycle.
    """

    class State(models.TextChoices):
        TO_ORDER = "TO_ORDER", "À commander"
        NEW_REQUEST = "NEW_REQUEST", "Nouvelle demande"
        REGISTERED = "REGISTERED", "Inscrit"
        DECOMMISSIONED = "DECOMMISSIONED", "Déclassé"

    license_plate = models.CharField(
        max_length=20, unique=True,
        help_text="Registration / plaque d'immatriculation. e.g. LT 1234 AB"
    )
    vin = models.CharField(
        max_length=50, unique=True,
        verbose_name="VIN / Chassis Number",
        help_text="Vehicle Identification Number (numéro de châssis)"
    )

    vehicle_model = models.ForeignKey(
        VehicleModel, on_delete=models.PROTECT, related_name="vehicles"
    )
    category = models.ForeignKey(
        "config.VehicleCategory", on_delete=models.PROTECT, related_name="vehicles",
        help_text="Fleet category: Utilitaire, Berline, Bus, etc."
    )

    driver = models.ForeignKey(
        "people.Driver", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="assigned_vehicles",
        help_text="Currently assigned driver"
    )
    fleet_manager = models.ForeignKey(
        "auth.User", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="managed_vehicles",
        help_text="Employee responsible for managing this vehicle"
    )
    tags = models.ManyToManyField(
        "config.Tag", blank=True, related_name="vehicles",
        help_text="Labels / étiquettes for grouping and filtering"
    )

    parking = models.ForeignKey(
        Parking, null=True, blank=True,
        on_delete=models.SET_NULL, related_name="vehicles",
        help_text="Current parking / emplacement"
    )

    order_date = models.DateField(
        null=True, blank=True, help_text="Date the vehicle was ordered"
    )
    registration_date = models.DateField(
        null=True, blank=True, help_text="Date d'immatriculation"
    )
    cancellation_date = models.DateField(
        null=True, blank=True,
        help_text="Date when the registration was cancelled/annulled"
    )
    first_contract_date = models.DateField(
        null=True, blank=True, help_text="Première date de contrat"
    )

    fiscal_horsepower = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True,
        help_text="Taxe sur la puissance (chevaux fiscaux)"
    )
    catalog_value = models.DecimalField(
        max_digits=18, decimal_places=2, null=True, blank=True,
        help_text="Valeur catalogue TTC (toutes taxes comprises)"
    )
    purchase_value = models.DecimalField(
        max_digits=18, decimal_places=2, null=True, blank=True,
        help_text="Valeur d'achat"
    )
    residual_value = models.DecimalField(
        max_digits=18, decimal_places=2, null=True, blank=True,
        help_text="Valeur résiduelle estimée"
    )

    state = models.CharField(
        max_length=20, choices=State.choices, default=State.NEW_REQUEST
    )
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["license_plate"]

    def __str__(self):
        return f"{self.license_plate} — {self.vehicle_model}"


class OdometerReading(BaseModel):
    """
    Recorded mileage / odometer snapshot for a vehicle.
    Used to track usage, trigger maintenance, and calculate costs per km.
    """
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="odometer_readings")
    date = models.DateField()
    value = models.DecimalField(
        max_digits=12, decimal_places=2,
        help_text="Odometer value at reading time"
    )
    unit = models.ForeignKey(
        "config.Unit", on_delete=models.PROTECT,
        help_text="Distance unit: km or mi"
    )
    notes = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["vehicle", "-date"]

    def __str__(self):
        return f"{self.vehicle.license_plate} — {self.value} {self.unit.code} ({self.date})"



class VehicleDocument(BaseModel):
    """
    Administrative document attached to a vehicle.
    Type is configurable via DocumentType (not hardcoded).
    Tracks expiration for alerts (insurance, technical inspection, etc.).
    """

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Actif"
        INACTIVE = "INACTIVE", "Inactif"

    document_type = models.ForeignKey(
        "config.DocumentType", on_delete=models.PROTECT, related_name="vehicle_documents"
    )
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="documents")
    reference_number = models.CharField(max_length=100, blank=True, help_text="Document reference / number")
    issue_date = models.DateField(null=True, blank=True, help_text="Date d'émission")
    expiry_date = models.DateField(
        null=True, blank=True,
        help_text="Date d'expiration. Required if the document type requires expiration."
    )
    file = models.FileField(upload_to="vehicle_documents/", null=True, blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        ordering = ["vehicle", "document_type", "-issue_date"]

    def __str__(self):
        return f"{self.vehicle.license_plate} — {self.document_type.label}"

    @property
    def is_expired(self):
        if self.expiry_date:
            import datetime
            return self.expiry_date < datetime.date.today()
        return False


class VehicleLayout(BaseModel):
    """
    Seating config / layout for a vehicle (especially buses).
    A vehicle has one active layout at a time, but multiple can be created
    for config changes. Example: 'Standard 50 places', 'VIP 30 places'.
    """
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="layouts")
    name = models.CharField(max_length=255, help_text="e.g. Standard 50 places, VIP 30 places")
    total_seats = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(
        default=False,
        help_text="Only one layout per vehicle should be active at a time."
    )

    class Meta:
        ordering = ["vehicle", "-is_active", "name"]

    def __str__(self):
        active = " (active)" if self.is_active else ""
        return f"{self.vehicle.license_plate} — {self.name}{active}"


class Seat(BaseModel):
    """
    Individual seat within a vehicle layout.
    Position is defined by row + column. Type distinguishes VIP, standard, driver.
    """

    class SeatType(models.TextChoices):
        STANDARD = "STANDARD", "Standard"
        VIP = "VIP", "VIP"
        DRIVER = "DRIVER", "Conducteur"

    layout = models.ForeignKey(VehicleLayout, on_delete=models.CASCADE, related_name="seats")
    seat_number = models.CharField(max_length=10, help_text="Seat identifier. e.g. A1, B3, 12")
    row = models.PositiveSmallIntegerField()
    column = models.PositiveSmallIntegerField()
    seat_type = models.CharField(
        max_length=10, choices=SeatType.choices, default=SeatType.STANDARD
    )
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = ("layout", "seat_number")
        ordering = ["layout", "row", "column"]

    def __str__(self):
        return f"Seat {self.seat_number} ({self.get_seat_type_display()})"

