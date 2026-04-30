from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Service, ServiceAttachment, Contract, RecurringCost
from . import selectors, services

from django.shortcuts import redirect


# ---------------------------------------------------------------------------
# Service
# ---------------------------------------------------------------------------
class ServiceListView(LoginRequiredMixin, ListView):
    template_name = "operations/service_list.html"
    context_object_name = "services"

    def get_queryset(self):
        return selectors.get_all_services()


class ServiceDetailView(LoginRequiredMixin, DetailView):
    template_name = "operations/service_detail.html"
    context_object_name = "service"

    def get_object(self):
        return selectors.get_service_by_id(service_id=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["attachments"] = selectors.get_attachments_for_service(service_id=self.object.id)
        return context


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    template_name = "operations/service_form.html"
    fields = [
        "description", "vehicle", "intervention_type", "date",
        "supplier", "cost", "currency", "notes",
        "driver", "status", "odometer_reading",
    ]
    success_url = reverse_lazy("operations:service-list")

    def form_valid(self, form):
        self.object = services.create_service(
            data=form.cleaned_data,
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Service
    template_name = "operations/service_form.html"
    fields = [
        "description", "vehicle", "intervention_type", "date",
        "supplier", "cost", "currency", "notes",
        "driver", "status", "odometer_reading",
    ]
    success_url = reverse_lazy("operations:service-list")

    def form_valid(self, form):
        services.update_service(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Service
    template_name = "operations/service_confirm_delete.html"
    success_url = reverse_lazy("operations:service-list")

    def form_valid(self, form):
        services.delete_service(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# ServiceAttachment
# ---------------------------------------------------------------------------
class ServiceAttachmentCreateView(LoginRequiredMixin, CreateView):
    model = ServiceAttachment
    template_name = "operations/service_attachment_form.html"
    fields = ["service", "file", "file_name", "description"]

    def get_success_url(self):
        return reverse_lazy("operations:service-detail", kwargs={"pk": self.kwargs.get("service_pk")})

    def get_initial(self):
        initial = super().get_initial()
        if "service_pk" in self.kwargs:
            initial["service"] = self.kwargs["service_pk"]
        return initial

    def form_valid(self, form):
        self.object = services.create_service_attachment(
            service_id=form.cleaned_data["service"].id,
            file=form.cleaned_data["file"],
            file_name=form.cleaned_data.get("file_name", ""),
            description=form.cleaned_data.get("description", ""),
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class ServiceAttachmentDeleteView(LoginRequiredMixin, DeleteView):
    model = ServiceAttachment
    template_name = "operations/service_attachment_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("operations:service-detail", kwargs={"pk": self.object.service_id})

    def form_valid(self, form):
        services.delete_service_attachment(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# Contract
# ---------------------------------------------------------------------------
class ContractListView(LoginRequiredMixin, ListView):
    template_name = "operations/contract_list.html"
    context_object_name = "contracts"

    def get_queryset(self):
        return selectors.get_all_contracts()


class ContractDetailView(LoginRequiredMixin, DetailView):
    template_name = "operations/contract_detail.html"
    context_object_name = "contract"

    def get_object(self):
        return selectors.get_contract_by_id(contract_id=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recurring_costs"] = selectors.get_recurring_costs_for_contract(contract_id=self.object.id)
        return context


class ContractCreateView(LoginRequiredMixin, CreateView):
    model = Contract
    template_name = "operations/contract_form.html"
    fields = [
        "name", "reference", "intervention_type", "included_services",
        "supplier", "start_date", "end_date", "creation_date",
        "responsible", "vehicle", "driver",
        "activation_cost", "billing_period", "currency",
        "status", "terms",
    ]
    success_url = reverse_lazy("operations:contract-list")

    def form_valid(self, form):
        self.object = services.create_contract(
            data=form.cleaned_data,
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class ContractUpdateView(LoginRequiredMixin, UpdateView):
    model = Contract
    template_name = "operations/contract_form.html"
    fields = [
        "name", "reference", "intervention_type", "included_services",
        "supplier", "start_date", "end_date", "creation_date",
        "responsible", "vehicle", "driver",
        "activation_cost", "billing_period", "currency",
        "status", "terms",
    ]
    success_url = reverse_lazy("operations:contract-list")

    def form_valid(self, form):
        services.update_contract(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class ContractDeleteView(LoginRequiredMixin, DeleteView):
    model = Contract
    template_name = "operations/contract_confirm_delete.html"
    success_url = reverse_lazy("operations:contract-list")

    def form_valid(self, form):
        services.delete_contract(instance=self.get_object())
        return redirect(self.get_success_url())


# ---------------------------------------------------------------------------
# RecurringCost
# ---------------------------------------------------------------------------
class RecurringCostListView(LoginRequiredMixin, ListView):
    template_name = "operations/recurring_cost_list.html"
    context_object_name = "recurring_costs"

    def get_queryset(self):
        return selectors.get_recurring_costs_for_contract(contract_id=self.kwargs["contract_pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contract"] = selectors.get_contract_by_id(contract_id=self.kwargs["contract_pk"])
        return context


class RecurringCostDetailView(LoginRequiredMixin, DetailView):
    template_name = "operations/recurring_cost_detail.html"
    context_object_name = "recurring_cost"

    def get_object(self):
        return selectors.get_recurring_cost_by_id(recurring_cost_id=self.kwargs["pk"])


class RecurringCostCreateView(LoginRequiredMixin, CreateView):
    model = RecurringCost
    template_name = "operations/recurring_cost_form.html"
    fields = ["contract", "description", "amount", "currency", "period"]

    def get_success_url(self):
        return reverse_lazy("operations:contract-detail", kwargs={"pk": self.kwargs.get("contract_pk")})

    def get_initial(self):
        initial = super().get_initial()
        if "contract_pk" in self.kwargs:
            initial["contract"] = self.kwargs["contract_pk"]
        return initial

    def form_valid(self, form):
        self.object = services.create_recurring_cost(
            contract_id=form.cleaned_data["contract"].id,
            description=form.cleaned_data["description"],
            amount=form.cleaned_data["amount"],
            currency=form.cleaned_data.get("currency", "XAF"),
            period_id=form.cleaned_data["period"].id,
            created_by=self.request.user,
        )
        return redirect(self.get_success_url())


class RecurringCostUpdateView(LoginRequiredMixin, UpdateView):
    model = RecurringCost
    template_name = "operations/recurring_cost_form.html"
    fields = ["contract", "description", "amount", "currency", "period"]
    success_url = reverse_lazy("operations:contract-list")

    def form_valid(self, form):
        services.update_recurring_cost(
            instance=self.get_object(),
            data=form.cleaned_data,
        )
        return redirect(self.get_success_url())


class RecurringCostDeleteView(LoginRequiredMixin, DeleteView):
    model = RecurringCost
    template_name = "operations/recurring_cost_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("operations:contract-detail", kwargs={"pk": self.object.contract_id})

    def form_valid(self, form):
        services.delete_recurring_cost(instance=self.get_object())
        return redirect(self.get_success_url())
