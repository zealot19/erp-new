from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import VehicleModel, Parking, Vehicle, OdometerReading, VehicleDocument, VehicleLayout, Seat
from . import selectors, services

from django.shortcuts import redirect


# ---------------------------------------------------------------------------
# VehicleModel
# ---------------------------------------------------------------------------
class VehicleModelListView(LoginRequiredMixin, ListView):
    template_name = "vehicles/vehicle_model_list.html"
    context_object_name = "vehicle_models"

    def get_queryset(self):
        return selectors.get_all_vehicle_models()


class VehicleModelDetailView(LoginRequiredMixin, DetailView):
    template_name = "vehicles/vehicle_model_detail.html"
    context_object_name = "vehicle_model"

    def get_object(self):
        return selectors.get_vehicle_model_by_id(vehicle_model_id=self.kwargs["pk"])


class VehicleModelCreateView(LoginRequiredMixin, CreateView):
    model = VehicleModel
    template_name = "vehicles/vehicle_model_form.html"
    fields = [
        "image", "vehicle_type", "manufacturer", "name", "model_year",
        "seats", "doors", "color", "has_tow_hitch",
        "fuel_type", "transmission", "traction_type",
        "power", "power_unit", "range_value", "range_unit",
        "co2_emission", "emission_unit", "emission_standard", "suppliers",
    ]
    success_url = reverse_lazy("vehicles:vehicle-model-list")

    def form_valid(self, form):
        self.object = services.create_vehicle_model(
            data=form.cleaned_data,
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class VehicleModelUpdateView(LoginRequiredMixin, UpdateView):
    model = VehicleModel
    template_name = "vehicles/vehicle_model_form.html"
    fields = [
        "image", "vehicle_type", "manufacturer", "name", "model_year",
        "seats", "doors", "color", "has_tow_hitch",
        "fuel_type", "transmission", "traction_type",
        "power", "power_unit", "range_value", "range_unit",
        "co2_emission", "emission_unit", "emission_standard", "suppliers",
    ]
    success_url = reverse_lazy("vehicles:vehicle-model-list")

    def form_valid(self, form):
        services.update_vehicle_model(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class VehicleModelDeleteView(LoginRequiredMixin, DeleteView):
    model = VehicleModel
    template_name = "vehicles/vehicle_model_confirm_delete.html"
    success_url = reverse_lazy("vehicles:vehicle-model-list")

    def form_valid(self, form):
        services.delete_vehicle_model(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# Parking
# ---------------------------------------------------------------------------
class ParkingListView(LoginRequiredMixin, ListView):
    template_name = "vehicles/parking_list.html"
    context_object_name = "parkings"

    def get_queryset(self):
        return selectors.get_all_parkings()


class ParkingDetailView(LoginRequiredMixin, DetailView):
    template_name = "vehicles/parking_detail.html"
    context_object_name = "parking"

    def get_object(self):
        return selectors.get_parking_by_id(parking_id=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vehicles"] = selectors.get_vehicles_by_parking(parking_id=self.object.id)
        return context


class ParkingCreateView(LoginRequiredMixin, CreateView):
    model = Parking
    template_name = "vehicles/parking_form.html"
    fields = ["name", "location", "notes"]
    success_url = reverse_lazy("vehicles:parking-list")

    def form_valid(self, form):
        self.object = services.create_parking(
            name=form.cleaned_data["name"],
            location=form.cleaned_data.get("location", ""),
            notes=form.cleaned_data.get("notes", ""),
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class ParkingUpdateView(LoginRequiredMixin, UpdateView):
    model = Parking
    template_name = "vehicles/parking_form.html"
    fields = ["name", "location", "notes"]
    success_url = reverse_lazy("vehicles:parking-list")

    def form_valid(self, form):
        services.update_parking(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class ParkingDeleteView(LoginRequiredMixin, DeleteView):
    model = Parking
    template_name = "vehicles/parking_confirm_delete.html"
    success_url = reverse_lazy("vehicles:parking-list")

    def form_valid(self, form):
        services.delete_parking(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# Vehicle
# ---------------------------------------------------------------------------
class VehicleListView(LoginRequiredMixin, ListView):
    template_name = "vehicles/vehicle_list.html"
    context_object_name = "vehicles"

    def get_queryset(self):
        return selectors.get_all_vehicles()


class VehicleDetailView(LoginRequiredMixin, DetailView):
    template_name = "vehicles/vehicle_detail.html"
    context_object_name = "vehicle"

    def get_object(self):
        return selectors.get_vehicle_by_id(vehicle_id=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["odometer_readings"] = selectors.get_odometer_readings_for_vehicle(vehicle_id=self.object.id)
        context["documents"] = selectors.get_documents_for_vehicle(vehicle_id=self.object.id)
        context["layouts"] = selectors.get_layouts_for_vehicle(vehicle_id=self.object.id)
        return context


class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    template_name = "vehicles/vehicle_form.html"
    fields = [
        "license_plate", "vin", "vehicle_model", "category",
        "driver", "fleet_manager", "tags", "parking",
        "order_date", "registration_date", "cancellation_date", "first_contract_date",
        "fiscal_horsepower", "catalog_value", "purchase_value", "residual_value",
        "state", "notes",
    ]
    success_url = reverse_lazy("vehicles:vehicle-list")

    def form_valid(self, form):
        self.object = services.create_vehicle(
            data=form.cleaned_data,
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    template_name = "vehicles/vehicle_form.html"
    fields = [
        "license_plate", "vin", "vehicle_model", "category",
        "driver", "fleet_manager", "tags", "parking",
        "order_date", "registration_date", "cancellation_date", "first_contract_date",
        "fiscal_horsepower", "catalog_value", "purchase_value", "residual_value",
        "state", "notes",
    ]
    success_url = reverse_lazy("vehicles:vehicle-list")

    def form_valid(self, form):
        services.update_vehicle(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicle
    template_name = "vehicles/vehicle_confirm_delete.html"
    success_url = reverse_lazy("vehicles:vehicle-list")

    def form_valid(self, form):
        services.delete_vehicle(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# OdometerReading
# ---------------------------------------------------------------------------
class OdometerReadingListView(LoginRequiredMixin, ListView):
    template_name = "vehicles/odometer_reading_list.html"
    context_object_name = "readings"

    def get_queryset(self):
        return selectors.get_odometer_readings_for_vehicle(vehicle_id=self.kwargs["vehicle_pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vehicle"] = selectors.get_vehicle_by_id(vehicle_id=self.kwargs["vehicle_pk"])
        return context


class OdometerReadingDetailView(LoginRequiredMixin, DetailView):
    template_name = "vehicles/odometer_reading_detail.html"
    context_object_name = "reading"

    def get_object(self):
        return selectors.get_odometer_reading_by_id(reading_id=self.kwargs["pk"])


class OdometerReadingCreateView(LoginRequiredMixin, CreateView):
    model = OdometerReading
    template_name = "vehicles/odometer_reading_form.html"
    fields = ["vehicle", "date", "value", "unit", "notes"]

    def get_success_url(self):
        return reverse_lazy("vehicles:vehicle-detail", kwargs={"pk": self.kwargs.get("vehicle_pk")})

    def get_initial(self):
        initial = super().get_initial()
        if "vehicle_pk" in self.kwargs:
            initial["vehicle"] = self.kwargs["vehicle_pk"]
        return initial

    def form_valid(self, form):
        self.object = services.create_odometer_reading(
            data=form.cleaned_data,
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class OdometerReadingUpdateView(LoginRequiredMixin, UpdateView):
    model = OdometerReading
    template_name = "vehicles/odometer_reading_form.html"
    fields = ["vehicle", "date", "value", "unit", "notes"]
    success_url = reverse_lazy("vehicles:vehicle-list")

    def form_valid(self, form):
        services.update_odometer_reading(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class OdometerReadingDeleteView(LoginRequiredMixin, DeleteView):
    model = OdometerReading
    template_name = "vehicles/odometer_reading_confirm_delete.html"
    success_url = reverse_lazy("vehicles:vehicle-list")

    def form_valid(self, form):
        services.delete_odometer_reading(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# VehicleDocument
# ---------------------------------------------------------------------------
class VehicleDocumentListView(LoginRequiredMixin, ListView):
    template_name = "vehicles/vehicle_document_list.html"
    context_object_name = "documents"

    def get_queryset(self):
        return selectors.get_documents_for_vehicle(vehicle_id=self.kwargs["vehicle_pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vehicle"] = selectors.get_vehicle_by_id(vehicle_id=self.kwargs["vehicle_pk"])
        return context


class VehicleDocumentDetailView(LoginRequiredMixin, DetailView):
    template_name = "vehicles/vehicle_document_detail.html"
    context_object_name = "document"

    def get_object(self):
        return selectors.get_vehicle_document_by_id(document_id=self.kwargs["pk"])


class VehicleDocumentCreateView(LoginRequiredMixin, CreateView):
    model = VehicleDocument
    template_name = "vehicles/vehicle_document_form.html"
    fields = ["document_type", "vehicle", "reference_number", "issue_date", "expiry_date", "file", "status"]

    def get_success_url(self):
        return reverse_lazy("vehicles:vehicle-detail", kwargs={"pk": self.kwargs.get("vehicle_pk")})

    def get_initial(self):
        initial = super().get_initial()
        if "vehicle_pk" in self.kwargs:
            initial["vehicle"] = self.kwargs["vehicle_pk"]
        return initial

    def form_valid(self, form):
        self.object = services.create_vehicle_document(
            data=form.cleaned_data,
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class VehicleDocumentUpdateView(LoginRequiredMixin, UpdateView):
    model = VehicleDocument
    template_name = "vehicles/vehicle_document_form.html"
    fields = ["document_type", "vehicle", "reference_number", "issue_date", "expiry_date", "file", "status"]
    success_url = reverse_lazy("vehicles:vehicle-list")

    def form_valid(self, form):
        services.update_vehicle_document(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class VehicleDocumentDeleteView(LoginRequiredMixin, DeleteView):
    model = VehicleDocument
    template_name = "vehicles/vehicle_document_confirm_delete.html"
    success_url = reverse_lazy("vehicles:vehicle-list")

    def form_valid(self, form):
        services.delete_vehicle_document(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# VehicleLayout
# ---------------------------------------------------------------------------
class VehicleLayoutListView(LoginRequiredMixin, ListView):
    template_name = "vehicles/vehicle_layout_list.html"
    context_object_name = "layouts"

    def get_queryset(self):
        return selectors.get_layouts_for_vehicle(vehicle_id=self.kwargs["vehicle_pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vehicle"] = selectors.get_vehicle_by_id(vehicle_id=self.kwargs["vehicle_pk"])
        return context


class VehicleLayoutDetailView(LoginRequiredMixin, DetailView):
    template_name = "vehicles/vehicle_layout_detail.html"
    context_object_name = "layout"

    def get_object(self):
        return selectors.get_vehicle_layout_by_id(layout_id=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seats"] = selectors.get_seats_for_layout(layout_id=self.object.id)
        return context


class VehicleLayoutCreateView(LoginRequiredMixin, CreateView):
    model = VehicleLayout
    template_name = "vehicles/vehicle_layout_form.html"
    fields = ["vehicle", "name", "total_seats", "is_active"]

    def get_success_url(self):
        return reverse_lazy("vehicles:vehicle-detail", kwargs={"pk": self.kwargs.get("vehicle_pk")})

    def get_initial(self):
        initial = super().get_initial()
        if "vehicle_pk" in self.kwargs:
            initial["vehicle"] = self.kwargs["vehicle_pk"]
        return initial

    def form_valid(self, form):
        self.object = services.create_vehicle_layout(
            vehicle_id=form.cleaned_data["vehicle"].id,
            name=form.cleaned_data["name"],
            total_seats=form.cleaned_data["total_seats"],
            is_active=form.cleaned_data.get("is_active", False),
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class VehicleLayoutUpdateView(LoginRequiredMixin, UpdateView):
    model = VehicleLayout
    template_name = "vehicles/vehicle_layout_form.html"
    fields = ["vehicle", "name", "total_seats", "is_active"]
    success_url = reverse_lazy("vehicles:vehicle-list")

    def form_valid(self, form):
        services.update_vehicle_layout(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class VehicleLayoutDeleteView(LoginRequiredMixin, DeleteView):
    model = VehicleLayout
    template_name = "vehicles/vehicle_layout_confirm_delete.html"
    success_url = reverse_lazy("vehicles:vehicle-list")

    def form_valid(self, form):
        services.delete_vehicle_layout(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# Seat
# ---------------------------------------------------------------------------
class SeatListView(LoginRequiredMixin, ListView):
    template_name = "vehicles/seat_list.html"
    context_object_name = "seats"

    def get_queryset(self):
        return selectors.get_seats_for_layout(layout_id=self.kwargs["layout_pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["layout"] = selectors.get_vehicle_layout_by_id(layout_id=self.kwargs["layout_pk"])
        return context


class SeatDetailView(LoginRequiredMixin, DetailView):
    template_name = "vehicles/seat_detail.html"
    context_object_name = "seat"

    def get_object(self):
        return selectors.get_seat_by_id(seat_id=self.kwargs["pk"])


class SeatCreateView(LoginRequiredMixin, CreateView):
    model = Seat
    template_name = "vehicles/seat_form.html"
    fields = ["layout", "seat_number", "row", "column", "seat_type", "is_available"]

    def get_success_url(self):
        return reverse_lazy("vehicles:vehicle-layout-detail", kwargs={"pk": self.kwargs.get("layout_pk")})

    def get_initial(self):
        initial = super().get_initial()
        if "layout_pk" in self.kwargs:
            initial["layout"] = self.kwargs["layout_pk"]
        return initial

    def form_valid(self, form):
        self.object = services.create_seat(
            data=form.cleaned_data,
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class SeatUpdateView(LoginRequiredMixin, UpdateView):
    model = Seat
    template_name = "vehicles/seat_form.html"
    fields = ["layout", "seat_number", "row", "column", "seat_type", "is_available"]
    success_url = reverse_lazy("vehicles:vehicle-list")

    def form_valid(self, form):
        services.update_seat(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class SeatDeleteView(LoginRequiredMixin, DeleteView):
    model = Seat
    template_name = "vehicles/seat_confirm_delete.html"
    success_url = reverse_lazy("vehicles:vehicle-list")

    def form_valid(self, form):
        services.delete_seat(instance=self.get_object())
        return redirect(self.get_success_url())
