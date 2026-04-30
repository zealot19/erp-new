from rest_framework.routers import DefaultRouter
from .views import DriverViewSet, SupplierViewSet, ManufacturerViewSet

app_name = "people_api"

router = DefaultRouter()
router.register("drivers", DriverViewSet, basename="driver")
router.register("suppliers", SupplierViewSet, basename="supplier")
router.register("manufacturers", ManufacturerViewSet, basename="manufacturer")

urlpatterns = router.urls
