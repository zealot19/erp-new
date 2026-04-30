from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect

from .models import (
    VehicleCategory, VehicleType, FuelType, Transmission, TractionType,
    UnitCategory, Unit, ActivitySector, Period, InterventionType,
    DocumentType, Tag,
)
from . import selectors, services


# ---------------------------------------------------------------------------
# VehicleCategory
# ---------------------------------------------------------------------------
class VehicleCategoryListView(LoginRequiredMixin, ListView):
    template_name = "configuration/vehicle_category_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return selectors.get_all_vehicle_categories()


class VehicleCategoryDetailView(LoginRequiredMixin, DetailView):
    template_name = "configuration/vehicle_category_detail.html"
    context_object_name = "category"

    def get_object(self):
        return selectors.get_vehicle_category_by_id(category_id=self.kwargs["pk"])


class VehicleCategoryCreateView(LoginRequiredMixin, CreateView):
    model = VehicleCategory
    template_name = "configuration/vehicle_category_form.html"
    fields = ["name"]
    success_url = reverse_lazy("configuration:vehicle-category-list")

    def form_valid(self, form):
        self.object = services.create_vehicle_category(
            name=form.cleaned_data["name"],
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class VehicleCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = VehicleCategory
    template_name = "configuration/vehicle_category_form.html"
    fields = ["name"]
    success_url = reverse_lazy("configuration:vehicle-category-list")

    def form_valid(self, form):
        services.update_vehicle_category(
            instance=self.get_object(),
            name=form.cleaned_data["name"],
        )
        return redirect(self.get_success_url())


class VehicleCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = VehicleCategory
    template_name = "configuration/vehicle_category_confirm_delete.html"
    success_url = reverse_lazy("configuration:vehicle-category-list")

    def form_valid(self, form):
        services.delete_vehicle_category(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# VehicleType
# ---------------------------------------------------------------------------
class VehicleTypeListView(LoginRequiredMixin, ListView):
    template_name = "configuration/vehicle_type_list.html"
    context_object_name = "vehicle_types"

    def get_queryset(self):
        return selectors.get_all_vehicle_types()


class VehicleTypeDetailView(LoginRequiredMixin, DetailView):
    template_name = "configuration/vehicle_type_detail.html"
    context_object_name = "vehicle_type"

    def get_object(self):
        return selectors.get_vehicle_type_by_id(type_id=self.kwargs["pk"])


class VehicleTypeCreateView(LoginRequiredMixin, CreateView):
    model = VehicleType
    template_name = "configuration/vehicle_type_form.html"
    fields = ["name"]
    success_url = reverse_lazy("configuration:vehicle-type-list")

    def form_valid(self, form):
        self.object = services.create_vehicle_type(
            name=form.cleaned_data["name"],
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class VehicleTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = VehicleType
    template_name = "configuration/vehicle_type_form.html"
    fields = ["name"]
    success_url = reverse_lazy("configuration:vehicle-type-list")

    def form_valid(self, form):
        services.update_vehicle_type(
            instance=self.get_object(),
            name=form.cleaned_data["name"],
        )
        return redirect(self.get_success_url())


class VehicleTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = VehicleType
    template_name = "configuration/vehicle_type_confirm_delete.html"
    success_url = reverse_lazy("configuration:vehicle-type-list")

    def form_valid(self, form):
        services.delete_vehicle_type(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# FuelType
# ---------------------------------------------------------------------------
class FuelTypeListView(LoginRequiredMixin, ListView):
    template_name = "configuration/fuel_type_list.html"
    context_object_name = "fuel_types"

    def get_queryset(self):
        return selectors.get_all_fuel_types()


class FuelTypeDetailView(LoginRequiredMixin, DetailView):
    template_name = "configuration/fuel_type_detail.html"
    context_object_name = "fuel_type"

    def get_object(self):
        return selectors.get_fuel_type_by_id(fuel_type_id=self.kwargs["pk"])


class FuelTypeCreateView(LoginRequiredMixin, CreateView):
    model = FuelType
    template_name = "configuration/fuel_type_form.html"
    fields = ["name"]
    success_url = reverse_lazy("configuration:fuel-type-list")

    def form_valid(self, form):
        self.object = services.create_fuel_type(
            name=form.cleaned_data["name"],
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class FuelTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = FuelType
    template_name = "configuration/fuel_type_form.html"
    fields = ["name"]
    success_url = reverse_lazy("configuration:fuel-type-list")

    def form_valid(self, form):
        services.update_fuel_type(
            instance=self.get_object(),
            name=form.cleaned_data["name"],
        )
        return redirect(self.get_success_url())


class FuelTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = FuelType
    template_name = "configuration/fuel_type_confirm_delete.html"
    success_url = reverse_lazy("configuration:fuel-type-list")

    def form_valid(self, form):
        services.delete_fuel_type(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# Transmission
# ---------------------------------------------------------------------------
class TransmissionListView(LoginRequiredMixin, ListView):
    template_name = "configuration/transmission_list.html"
    context_object_name = "transmissions"

    def get_queryset(self):
        return selectors.get_all_transmissions()


class TransmissionDetailView(LoginRequiredMixin, DetailView):
    template_name = "configuration/transmission_detail.html"
    context_object_name = "transmission"

    def get_object(self):
        return selectors.get_transmission_by_id(transmission_id=self.kwargs["pk"])


class TransmissionCreateView(LoginRequiredMixin, CreateView):
    model = Transmission
    template_name = "configuration/transmission_form.html"
    fields = ["name"]
    success_url = reverse_lazy("configuration:transmission-list")

    def form_valid(self, form):
        self.object = services.create_transmission(
            name=form.cleaned_data["name"],
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class TransmissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transmission
    template_name = "configuration/transmission_form.html"
    fields = ["name"]
    success_url = reverse_lazy("configuration:transmission-list")

    def form_valid(self, form):
        services.update_transmission(
            instance=self.get_object(),
            name=form.cleaned_data["name"],
        )
        return redirect(self.get_success_url())


class TransmissionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transmission
    template_name = "configuration/transmission_confirm_delete.html"
    success_url = reverse_lazy("configuration:transmission-list")

    def form_valid(self, form):
        services.delete_transmission(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# TractionType
# ---------------------------------------------------------------------------
class TractionTypeListView(LoginRequiredMixin, ListView):
    template_name = "configuration/traction_type_list.html"
    context_object_name = "traction_types"

    def get_queryset(self):
        return selectors.get_all_traction_types()


class TractionTypeDetailView(LoginRequiredMixin, DetailView):
    template_name = "configuration/traction_type_detail.html"
    context_object_name = "traction_type"

    def get_object(self):
        return selectors.get_traction_type_by_id(traction_type_id=self.kwargs["pk"])


class TractionTypeCreateView(LoginRequiredMixin, CreateView):
    model = TractionType
    template_name = "configuration/traction_type_form.html"
    fields = ["name"]
    success_url = reverse_lazy("configuration:traction-type-list")

    def form_valid(self, form):
        self.object = services.create_traction_type(
            name=form.cleaned_data["name"],
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class TractionTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = TractionType
    template_name = "configuration/traction_type_form.html"
    fields = ["name"]
    success_url = reverse_lazy("configuration:traction-type-list")

    def form_valid(self, form):
        services.update_traction_type(
            instance=self.get_object(),
            name=form.cleaned_data["name"],
        )
        return redirect(self.get_success_url())


class TractionTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = TractionType
    template_name = "configuration/traction_type_confirm_delete.html"
    success_url = reverse_lazy("configuration:traction-type-list")

    def form_valid(self, form):
        services.delete_traction_type(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# UnitCategory
# ---------------------------------------------------------------------------
class UnitCategoryListView(LoginRequiredMixin, ListView):
    template_name = "configuration/unit_category_list.html"
    context_object_name = "unit_categories"

    def get_queryset(self):
        return selectors.get_all_unit_categories()


class UnitCategoryDetailView(LoginRequiredMixin, DetailView):
    template_name = "configuration/unit_category_detail.html"
    context_object_name = "unit_category"

    def get_object(self):
        return selectors.get_unit_category_by_id(unit_category_id=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["units"] = selectors.get_units_by_category(category_id=self.object.id)
        return context


class UnitCategoryCreateView(LoginRequiredMixin, CreateView):
    model = UnitCategory
    template_name = "configuration/unit_category_form.html"
    fields = ["name"]
    success_url = reverse_lazy("configuration:unit-category-list")

    def form_valid(self, form):
        self.object = services.create_unit_category(
            name=form.cleaned_data["name"],
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class UnitCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = UnitCategory
    template_name = "configuration/unit_category_form.html"
    fields = ["name"]
    success_url = reverse_lazy("configuration:unit-category-list")

    def form_valid(self, form):
        services.update_unit_category(
            instance=self.get_object(),
            name=form.cleaned_data["name"],
        )
        return redirect(self.get_success_url())


class UnitCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = UnitCategory
    template_name = "configuration/unit_category_confirm_delete.html"
    success_url = reverse_lazy("configuration:unit-category-list")

    def form_valid(self, form):
        services.delete_unit_category(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# Unit
# ---------------------------------------------------------------------------
class UnitListView(LoginRequiredMixin, ListView):
    template_name = "configuration/unit_list.html"
    context_object_name = "units"

    def get_queryset(self):
        return selectors.get_all_units()


class UnitDetailView(LoginRequiredMixin, DetailView):
    template_name = "configuration/unit_detail.html"
    context_object_name = "unit"

    def get_object(self):
        return selectors.get_unit_by_id(unit_id=self.kwargs["pk"])


class UnitCreateView(LoginRequiredMixin, CreateView):
    model = Unit
    template_name = "configuration/unit_form.html"
    fields = ["category", "code", "name"]
    success_url = reverse_lazy("configuration:unit-list")

    def form_valid(self, form):
        self.object = services.create_unit(
            category_id=form.cleaned_data["category"].id,
            code=form.cleaned_data["code"],
            name=form.cleaned_data["name"],
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class UnitUpdateView(LoginRequiredMixin, UpdateView):
    model = Unit
    template_name = "configuration/unit_form.html"
    fields = ["category", "code", "name"]
    success_url = reverse_lazy("configuration:unit-list")

    def form_valid(self, form):
        services.update_unit(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class UnitDeleteView(LoginRequiredMixin, DeleteView):
    model = Unit
    template_name = "configuration/unit_confirm_delete.html"
    success_url = reverse_lazy("configuration:unit-list")

    def form_valid(self, form):
        services.delete_unit(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# ActivitySector
# ---------------------------------------------------------------------------
class ActivitySectorListView(LoginRequiredMixin, ListView):
    template_name = "configuration/activity_sector_list.html"
    context_object_name = "sectors"

    def get_queryset(self):
        return selectors.get_all_activity_sectors()


class ActivitySectorDetailView(LoginRequiredMixin, DetailView):
    template_name = "configuration/activity_sector_detail.html"
    context_object_name = "sector"

    def get_object(self):
        return selectors.get_activity_sector_by_id(sector_id=self.kwargs["pk"])


class ActivitySectorCreateView(LoginRequiredMixin, CreateView):
    model = ActivitySector
    template_name = "configuration/activity_sector_form.html"
    fields = ["code", "name"]
    success_url = reverse_lazy("configuration:activity-sector-list")

    def form_valid(self, form):
        self.object = services.create_activity_sector(
            code=form.cleaned_data["code"],
            name=form.cleaned_data["name"],
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class ActivitySectorUpdateView(LoginRequiredMixin, UpdateView):
    model = ActivitySector
    template_name = "configuration/activity_sector_form.html"
    fields = ["code", "name"]
    success_url = reverse_lazy("configuration:activity-sector-list")

    def form_valid(self, form):
        services.update_activity_sector(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class ActivitySectorDeleteView(LoginRequiredMixin, DeleteView):
    model = ActivitySector
    template_name = "configuration/activity_sector_confirm_delete.html"
    success_url = reverse_lazy("configuration:activity-sector-list")

    def form_valid(self, form):
        services.delete_activity_sector(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# Period
# ---------------------------------------------------------------------------
class PeriodListView(LoginRequiredMixin, ListView):
    template_name = "configuration/period_list.html"
    context_object_name = "periods"

    def get_queryset(self):
        return selectors.get_all_periods()


class PeriodDetailView(LoginRequiredMixin, DetailView):
    template_name = "configuration/period_detail.html"
    context_object_name = "period"

    def get_object(self):
        return selectors.get_period_by_id(period_id=self.kwargs["pk"])


class PeriodCreateView(LoginRequiredMixin, CreateView):
    model = Period
    template_name = "configuration/period_form.html"
    fields = ["name"]
    success_url = reverse_lazy("configuration:period-list")

    def form_valid(self, form):
        self.object = services.create_period(
            name=form.cleaned_data["name"],
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class PeriodUpdateView(LoginRequiredMixin, UpdateView):
    model = Period
    template_name = "configuration/period_form.html"
    fields = ["name"]
    success_url = reverse_lazy("configuration:period-list")

    def form_valid(self, form):
        services.update_period(
            instance=self.get_object(),
            name=form.cleaned_data["name"],
        )
        return redirect(self.get_success_url())


class PeriodDeleteView(LoginRequiredMixin, DeleteView):
    model = Period
    template_name = "configuration/period_confirm_delete.html"
    success_url = reverse_lazy("configuration:period-list")

    def form_valid(self, form):
        services.delete_period(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# InterventionType
# ---------------------------------------------------------------------------
class InterventionTypeListView(LoginRequiredMixin, ListView):
    template_name = "configuration/intervention_type_list.html"
    context_object_name = "intervention_types"

    def get_queryset(self):
        return selectors.get_all_intervention_types()


class InterventionTypeDetailView(LoginRequiredMixin, DetailView):
    template_name = "configuration/intervention_type_detail.html"
    context_object_name = "intervention_type"

    def get_object(self):
        return selectors.get_intervention_type_by_id(intervention_type_id=self.kwargs["pk"])


class InterventionTypeCreateView(LoginRequiredMixin, CreateView):
    model = InterventionType
    template_name = "configuration/intervention_type_form.html"
    fields = ["name", "category"]
    success_url = reverse_lazy("configuration:intervention-type-list")

    def form_valid(self, form):
        self.object = services.create_intervention_type(
            name=form.cleaned_data["name"],
            category=form.cleaned_data["category"],
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class InterventionTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = InterventionType
    template_name = "configuration/intervention_type_form.html"
    fields = ["name", "category"]
    success_url = reverse_lazy("configuration:intervention-type-list")

    def form_valid(self, form):
        services.update_intervention_type(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class InterventionTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = InterventionType
    template_name = "configuration/intervention_type_confirm_delete.html"
    success_url = reverse_lazy("configuration:intervention-type-list")

    def form_valid(self, form):
        services.delete_intervention_type(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# DocumentType
# ---------------------------------------------------------------------------
class DocumentTypeListView(LoginRequiredMixin, ListView):
    template_name = "configuration/document_type_list.html"
    context_object_name = "document_types"

    def get_queryset(self):
        return selectors.get_all_document_types()


class DocumentTypeDetailView(LoginRequiredMixin, DetailView):
    template_name = "configuration/document_type_detail.html"
    context_object_name = "document_type"

    def get_object(self):
        return selectors.get_document_type_by_id(document_type_id=self.kwargs["pk"])


class DocumentTypeCreateView(LoginRequiredMixin, CreateView):
    model = DocumentType
    template_name = "configuration/document_type_form.html"
    fields = ["code", "label", "requires_expiration"]
    success_url = reverse_lazy("configuration:document-type-list")

    def form_valid(self, form):
        self.object = services.create_document_type(
            code=form.cleaned_data["code"],
            label=form.cleaned_data["label"],
            requires_expiration=form.cleaned_data.get("requires_expiration", True),
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class DocumentTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = DocumentType
    template_name = "configuration/document_type_form.html"
    fields = ["code", "label", "requires_expiration"]
    success_url = reverse_lazy("configuration:document-type-list")

    def form_valid(self, form):
        services.update_document_type(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class DocumentTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = DocumentType
    template_name = "configuration/document_type_confirm_delete.html"
    success_url = reverse_lazy("configuration:document-type-list")

    def form_valid(self, form):
        services.delete_document_type(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# Tag
# ---------------------------------------------------------------------------
class TagListView(LoginRequiredMixin, ListView):
    template_name = "configuration/tag_list.html"
    context_object_name = "tags"

    def get_queryset(self):
        return selectors.get_all_tags()


class TagDetailView(LoginRequiredMixin, DetailView):
    template_name = "configuration/tag_detail.html"
    context_object_name = "tag"

    def get_object(self):
        return selectors.get_tag_by_id(tag_id=self.kwargs["pk"])


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = "configuration/tag_form.html"
    fields = ["name", "color"]
    success_url = reverse_lazy("configuration:tag-list")

    def form_valid(self, form):
        self.object = services.create_tag(
            name=form.cleaned_data["name"],
            color=form.cleaned_data.get("color", ""),
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    template_name = "configuration/tag_form.html"
    fields = ["name", "color"]
    success_url = reverse_lazy("configuration:tag-list")

    def form_valid(self, form):
        services.update_tag(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = "configuration/tag_confirm_delete.html"
    success_url = reverse_lazy("configuration:tag-list")

    def form_valid(self, form):
        services.delete_tag(instance=self.get_object())
        return redirect(self.get_success_url())
