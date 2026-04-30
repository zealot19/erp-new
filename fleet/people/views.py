from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Driver, Supplier, Manufacturer
from . import selectors, services

from django.shortcuts import redirect


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
class DriverListView(LoginRequiredMixin, ListView):
    template_name = "people/driver_list.html"
    context_object_name = "drivers"

    def get_queryset(self):
        return selectors.get_all_drivers()


class DriverDetailView(LoginRequiredMixin, DetailView):
    template_name = "people/driver_detail.html"
    context_object_name = "driver"

    def get_object(self):
        return selectors.get_driver_by_id(driver_id=self.kwargs["pk"])


class DriverCreateView(LoginRequiredMixin, CreateView):
    model = Driver
    template_name = "people/driver_form.html"
    fields = [
        "user", "employee_id", "first_name", "last_name",
        "phone", "email", "license_number", "license_expiry",
        "license_category", "is_active",
    ]
    success_url = reverse_lazy("people:driver-list")

    def form_valid(self, form):
        self.object = services.create_driver(
            data=form.cleaned_data,
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class DriverUpdateView(LoginRequiredMixin, UpdateView):
    model = Driver
    template_name = "people/driver_form.html"
    fields = [
        "user", "employee_id", "first_name", "last_name",
        "phone", "email", "license_number", "license_expiry",
        "license_category", "is_active",
    ]
    success_url = reverse_lazy("people:driver-list")

    def form_valid(self, form):
        services.update_driver(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class DriverDeleteView(LoginRequiredMixin, DeleteView):
    model = Driver
    template_name = "people/driver_confirm_delete.html"
    success_url = reverse_lazy("people:driver-list")

    def form_valid(self, form):
        services.delete_driver(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# Supplier
# ---------------------------------------------------------------------------
class SupplierListView(LoginRequiredMixin, ListView):
    template_name = "people/supplier_list.html"
    context_object_name = "suppliers"

    def get_queryset(self):
        return selectors.get_all_suppliers()


class SupplierDetailView(LoginRequiredMixin, DetailView):
    template_name = "people/supplier_detail.html"
    context_object_name = "supplier"

    def get_object(self):
        return selectors.get_supplier_by_id(supplier_id=self.kwargs["pk"])


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    template_name = "people/supplier_form.html"
    fields = [
        "name", "code", "tax_id", "address", "city", "country",
        "phone", "email", "website", "contact_person", "notes", "is_active",
    ]
    success_url = reverse_lazy("people:supplier-list")

    def form_valid(self, form):
        self.object = services.create_supplier(
            data=form.cleaned_data,
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Supplier
    template_name = "people/supplier_form.html"
    fields = [
        "name", "code", "tax_id", "address", "city", "country",
        "phone", "email", "website", "contact_person", "notes", "is_active",
    ]
    success_url = reverse_lazy("people:supplier-list")

    def form_valid(self, form):
        services.update_supplier(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    template_name = "people/supplier_confirm_delete.html"
    success_url = reverse_lazy("people:supplier-list")

    def form_valid(self, form):
        services.delete_supplier(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# Manufacturer
# ---------------------------------------------------------------------------
class ManufacturerListView(LoginRequiredMixin, ListView):
    template_name = "people/manufacturer_list.html"
    context_object_name = "manufacturers"

    def get_queryset(self):
        return selectors.get_all_manufacturers()


class ManufacturerDetailView(LoginRequiredMixin, DetailView):
    template_name = "people/manufacturer_detail.html"
    context_object_name = "manufacturer"

    def get_object(self):
        return selectors.get_manufacturer_by_id(manufacturer_id=self.kwargs["pk"])


class ManufacturerCreateView(LoginRequiredMixin, CreateView):
    model = Manufacturer
    template_name = "people/manufacturer_form.html"
    fields = ["name", "country", "logo"]
    success_url = reverse_lazy("people:manufacturer-list")

    def form_valid(self, form):
        self.object = services.create_manufacturer(
            name=form.cleaned_data["name"],
            country=form.cleaned_data.get("country", ""),
            logo=form.cleaned_data.get("logo"),
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class ManufacturerUpdateView(LoginRequiredMixin, UpdateView):
    model = Manufacturer
    template_name = "people/manufacturer_form.html"
    fields = ["name", "country", "logo"]
    success_url = reverse_lazy("people:manufacturer-list")

    def form_valid(self, form):
        services.update_manufacturer(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class ManufacturerDeleteView(LoginRequiredMixin, DeleteView):
    model = Manufacturer
    template_name = "people/manufacturer_confirm_delete.html"
    success_url = reverse_lazy("people:manufacturer-list")

    def form_valid(self, form):
        services.delete_manufacturer(instance=self.get_object())
        return redirect(self.get_success_url())
