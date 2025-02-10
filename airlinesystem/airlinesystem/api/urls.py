from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AirplaneView, FlightView, ReservationView

router = DefaultRouter()
router.register(r"airplanes", AirplaneView)
router.register(r"flights", FlightView)
router.register(r"reservations", ReservationView)

urlpatterns = [
    path("", include(router.urls)),
]
