from django.urls import path, include
from . import views

app_name = "operations"

urlpatterns = [
    # --- Service ---
    path("services/", views.ServiceListView.as_view(), name="service-list"),
    path("services/<uuid:pk>/", views.ServiceDetailView.as_view(), name="service-detail"),
    path("services/create/", views.ServiceCreateView.as_view(), name="service-create"),
    path("services/<uuid:pk>/edit/", views.ServiceUpdateView.as_view(), name="service-update"),
    path("services/<uuid:pk>/delete/", views.ServiceDeleteView.as_view(), name="service-delete"),

    # --- ServiceAttachment (nested under service) ---
    path("services/<uuid:service_pk>/attachments/add/", views.ServiceAttachmentCreateView.as_view(), name="service-attachment-create"),
    path("attachments/<uuid:pk>/delete/", views.ServiceAttachmentDeleteView.as_view(), name="service-attachment-delete"),

    # --- Contract ---
    path("contracts/", views.ContractListView.as_view(), name="contract-list"),
    path("contracts/<uuid:pk>/", views.ContractDetailView.as_view(), name="contract-detail"),
    path("contracts/create/", views.ContractCreateView.as_view(), name="contract-create"),
    path("contracts/<uuid:pk>/edit/", views.ContractUpdateView.as_view(), name="contract-update"),
    path("contracts/<uuid:pk>/delete/", views.ContractDeleteView.as_view(), name="contract-delete"),

    # --- RecurringCost (nested under contract) ---
    path("contracts/<uuid:contract_pk>/costs/", views.RecurringCostListView.as_view(), name="recurring-cost-list"),
    path("contracts/<uuid:contract_pk>/costs/add/", views.RecurringCostCreateView.as_view(), name="recurring-cost-create"),
    path("costs/<uuid:pk>/", views.RecurringCostDetailView.as_view(), name="recurring-cost-detail"),
    path("costs/<uuid:pk>/edit/", views.RecurringCostUpdateView.as_view(), name="recurring-cost-update"),
    path("costs/<uuid:pk>/delete/", views.RecurringCostDeleteView.as_view(), name="recurring-cost-delete"),

    # --- API ---
    path("api/", include("fleet.operations.api.urls")),
]
