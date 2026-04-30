from django.db import models

#Here we can find all the core models needed in the ERP, which all other models depend on.
from django.db import models
import uuid


class BaseModel(models.Model):
    """Shared audit fields for every model in the system."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        "auth.User", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="+"
    )

    class Meta:
        abstract = True


class Person(BaseModel):
    """
    Abstract base for any human entity in the system.
    Contains only identity, contact, and personal data.
    """

    class Gender(models.TextChoices):
        MALE = "MALE", "Masculin"
        FEMALE = "FEMALE", "Feminin"
        OTHER = "OTHER", "Autre"
        UNDISCLOSED = "UNDISCLOSED", "Non precise"

    # ---- Identity ----
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    legal_name = models.CharField(max_length=255, blank=True, help_text="Nom légal / passeport")
    photo = models.ImageField(upload_to="persons/photos/", null=True, blank=True)
    gender = models.CharField(max_length=12, choices=Gender.choices, default=Gender.UNDISCLOSED)
    birthday = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=120, blank=True)
    nationality = models.CharField(max_length=120, blank=True)

    # ---- Identity Documents ----
    identification_no = models.CharField(max_length=120, blank=True, help_text="Numéro d'identité nationale")
    passport_no = models.CharField(max_length=120, blank=True)

    # ---- Contact ----
    phone = models.CharField(max_length=40, blank=True)
    mobile = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)

    # ---- Emergency ----
    emergency_contact_name = models.CharField(max_length=255, blank=True)
    emergency_contact_phone = models.CharField(max_length=40, blank=True)

    # ---- System User ----
    user = models.OneToOneField(
        "auth.User", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="%(class)s_profile",
        help_text="Utilisateur système lié"
    )

    class Meta:
        abstract = True
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

        
class Company(BaseModel):
    """
    Legal entity or business unit.
    Supports multi-company hierarchy via parent_company self-reference.
    """
    name = models.CharField(max_length=255, help_text="Nom de la societe")
    code = models.CharField(max_length=30, unique=True, help_text="Code identifiant court")
    street = models.CharField(max_length=255, blank=True)
    street2 = models.CharField(max_length=255, blank=True, verbose_name="Rue ligne 2")
    city = models.CharField(max_length=128, blank=True)
    state = models.CharField(max_length=128, blank=True, verbose_name="Etat ou province")
    zip_code = models.CharField(max_length=24, blank=True)
    country = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=64, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to="hr/companies/logos/", null=True, blank=True)
    currency = models.CharField(max_length=10, default="XAF", help_text="Devise par defaut")
    parent_company = models.ForeignKey(
        "self", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="subsidiaries",
        help_text="Societe parente"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "companies"
        ordering = ["name"]

    def __str__(self):
        return f"{self.code} — {self.name}"


class Address(BaseModel):
    """
    Reusable address record for work premises and private residences.
    """
    label = models.CharField(max_length=120, help_text="Libelle (ex: 'Siege')")
    street_1 = models.CharField(max_length=255)
    street_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120, blank=True, verbose_name="Etat ou province")
    postal_code = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=120, blank=True)

    class Meta:
        verbose_name_plural = "addresses"
        ordering = ["label"]

    def __str__(self):
        return f"{self.label} — {self.city}"


