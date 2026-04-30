from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, ServiceAttachmentViewSet, ContractViewSet, RecurringCostViewSet

app_name = "operations_api"

router = DefaultRouter()
router.register("services", ServiceViewSet, basename="service")
router.register("service-attachments", ServiceAttachmentViewSet, basename="service-attachment")
router.register("contracts", ContractViewSet, basename="contract")
router.register("recurring-costs", RecurringCostViewSet, basename="recurring-cost")

urlpatterns = router.urls
