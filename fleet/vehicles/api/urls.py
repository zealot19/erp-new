from rest_framework.routers import DefaultRouter
from .views import (
    VehicleModelViewSet, ParkingViewSet, VehicleViewSet,
    OdometerReadingViewSet, VehicleDocumentViewSet,
    VehicleLayoutViewSet, SeatViewSet,
)

app_name = "vehicles_api"

router = DefaultRouter()
router.register("models", VehicleModelViewSet, basename="vehicle-model")
router.register("parkings", ParkingViewSet, basename="parking")
router.register("vehicles", VehicleViewSet, basename="vehicle")
router.register("odometer-readings", OdometerReadingViewSet, basename="odometer-reading")
router.register("documents", VehicleDocumentViewSet, basename="vehicle-document")
router.register("layouts", VehicleLayoutViewSet, basename="vehicle-layout")
router.register("seats", SeatViewSet, basename="seat")

urlpatterns = router.urls
