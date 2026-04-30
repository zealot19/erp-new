"""
Operations — Services (Maintenance/Repairs) & Contracts
"""
from django.db import models
from core.models import BaseModel

class Service(BaseModel):
    """
    A one-time maintenance or repair intervention on a vehicle.
    Examples: Oil change, tyre replacement, brake repair, accident repair.
    """

    class Status(models.TextChoices):
        NEW = "NEW", "Nouveau"
        IN_PROGRESS = "IN_PROGRESS", "En cours"
        DONE = "DONE", "Terminé"
        CANCELLED = "CANCELLED", "Annulé"

    description = models.CharField(max_length=500)
    vehicle = models.ForeignKey(
        "vehicles.Vehicle", on_delete=models.CASCADE, related_name="services"
    )
    intervention_type = models.ForeignKey(
        "config.InterventionType", on_delete=models.PROTECT, related_name="services"
    )
    date = models.DateField(help_text="Date of the service / intervention")
    supplier = models.ForeignKey(
        "people.Supplier", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="services"
    )
    cost = models.DecimalField(
        max_digits=18, decimal_places=2, default=0,
        help_text="Total cost of the service"
    )
    currency = models.CharField(max_length=3, default="XAF")
    notes = models.TextField(blank=True)
    driver = models.ForeignKey(
        "people.Driver", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="services",
        help_text="Driver at the time of the service"
    )
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.NEW)
    odometer_reading = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True,
        help_text="Odometer value at time of service"
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.vehicle.license_plate} — {self.description} ({self.date})"


class ServiceAttachment(BaseModel):
    """
    File attachment linked to a service record.
    Examples: invoices, photos, reports.
    """
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="attachments")
    file = models.FileField(upload_to="service_attachments/")
    file_name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["service", "created_at"]

    def __str__(self):
        return f"Attachment: {self.file_name or self.file.name}"


class Contract(BaseModel):
    """
    A recurring contract linked to a vehicle.
    Examples: Insurance policy, leasing agreement, maintenance plan,
    parking subscription, fuel card.
    """

    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Brouillon"
        ACTIVE = "ACTIVE", "Actif"
        EXPIRED = "EXPIRED", "Expiré"
        CANCELLED = "CANCELLED", "Annulé"

    name = models.CharField(max_length=255, help_text="Contract name / title")
    reference = models.CharField(max_length=100, blank=True, help_text="External contract reference")
    intervention_type = models.ForeignKey(
        "config.InterventionType", on_delete=models.PROTECT,
        related_name="contracts",
        help_text="Primary intervention type for this contract"
    )
    included_services = models.ManyToManyField(
        "config.InterventionType", blank=True,
        related_name="included_in_contracts",
        help_text="Intervention types covered / included in this contract"
    )
    supplier = models.ForeignKey(
        "people.Supplier", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="contracts",
        help_text="Supplier / société associée providing this contract"
    )

    # --- Dates ---
    start_date = models.DateField(help_text="Date de début du contrat")
    end_date = models.DateField(help_text="Date de fin du contrat", null=True, blank=True)
    creation_date = models.DateField(
        null=True, blank=True,
        help_text="Date de création du contrat (when the contract was signed)"
    )

    # --- Assignment ---
    responsible = models.ForeignKey(
        "auth.User", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="managed_contracts",
        help_text="Internal person responsible for this contract"
    )
    vehicle = models.ForeignKey(
        "vehicles.Vehicle", on_delete=models.CASCADE, related_name="contracts"
    )
    driver = models.ForeignKey(
        "people.Driver", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="contracts",
        help_text="Driver assigned to this contract"
    )

    # --- Financial ---
    activation_cost = models.DecimalField(
        max_digits=18, decimal_places=2, default=0,
        help_text="One-time activation / setup cost (coûts d'activation)"
    )
    billing_period = models.ForeignKey(
        "config.Period", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="contracts",
        help_text="Billing frequency: Mensuel, Trimestriel, Annuel"
    )
    currency = models.CharField(max_length=3, default="XAF")

    # --- Status & Notes ---
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.DRAFT)
    terms = models.TextField(
        blank=True,
        help_text="Conditions générales: all information concerning the contract"
    )

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.name} — {self.vehicle.license_plate}"

    @property
    def is_expired(self):
        import datetime
        if self.end_date is None:
            return False  # or True, depending on logic
        return self.end_date < datetime.date.today()


class RecurringCost(BaseModel):
    """
    A recurring cost line within a contract.
    Examples: Monthly lease payment, quarterly insurance premium.
    """
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name="recurring_costs")
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    currency = models.CharField(max_length=3, default="XAF")
    period = models.ForeignKey(
        "config.Period", on_delete=models.PROTECT,
        help_text="Recurrence frequency for this cost"
    )

    class Meta:
        ordering = ["contract", "description"]

    def __str__(self):
        return f"{self.description} — {self.amount} {self.currency}/{self.period.name}"


