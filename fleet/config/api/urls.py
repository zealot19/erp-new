from rest_framework.routers import DefaultRouter
from .views import (
    VehicleCategoryViewSet, VehicleTypeViewSet, FuelTypeViewSet,
    TransmissionViewSet, TractionTypeViewSet, UnitCategoryViewSet,
    UnitViewSet, ActivitySectorViewSet, PeriodViewSet,
    InterventionTypeViewSet, DocumentTypeViewSet, TagViewSet,
)

app_name = "configuration_api"

router = DefaultRouter()
router.register("vehicle-categories", VehicleCategoryViewSet, basename="vehicle-category")
router.register("vehicle-types", VehicleTypeViewSet, basename="vehicle-type")
router.register("fuel-types", FuelTypeViewSet, basename="fuel-type")
router.register("transmissions", TransmissionViewSet, basename="transmission")
router.register("traction-types", TractionTypeViewSet, basename="traction-type")
router.register("unit-categories", UnitCategoryViewSet, basename="unit-category")
router.register("units", UnitViewSet, basename="unit")
router.register("activity-sectors", ActivitySectorViewSet, basename="activity-sector")
router.register("periods", PeriodViewSet, basename="period")
router.register("intervention-types", InterventionTypeViewSet, basename="intervention-type")
router.register("document-types", DocumentTypeViewSet, basename="document-type")
router.register("tags", TagViewSet, basename="tag")

urlpatterns = router.urls
