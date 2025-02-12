from django.shortcuts import render
from rest_framework import viewsets
from .models import Airplane, Flight, Reservation
from .serializers import AirplaneSerializer, FlightSerializer, ReservationSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import FlightFilter


class AirplaneView(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    @action(detail=True, methods=["GET"])
    def flights(self, request, pk=None):

        try:
            airplane_info = Airplane.objects.get(pk=pk)
        except Airplane.DoesNotExist:
            return Response(
                {"error": "Airplane not found"}, status=status.HTTP_404_NOT_FOUND
            )

        flights = Flight.objects.filter(airplane=airplane_info)
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)


class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_class = FlightFilter
    ordering_fields = ["departure_time", "arrival_time"]
    search_fields = ["departure", "destination"]

    @action(detail=True, methods=["GET"])
    def reservation(self, request, pk=None):
        try:
            flight_info = Flight.objects.get(pk=pk)
        except Flight.DoesNotExist:
            return Response(
                {"error": "Flight not found"}, status=status.HTTP_404_NOT_FOUND
            )

        reservations = Reservation.objects.filter(flight=flight_info)
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)


class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):

        flight_id = request.data.get("flight")

        try:
            flight = Flight.objects.get(id=flight_id)
        except Flight.DoesNotExist:
            return Response(
                {"error": "Flight not found."}, status=status.HTTP_404_NOT_FOUND
            )

        active_reservations = flight.reservations.filter(status=True).count()
        if active_reservations >= flight.airplane.capacity:
            return Response(
                {"error": "This flight is fully booked."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=["GET"])
    def available_reservations(self, request):

        available_reservations = Reservation.objects.filter(
            flight__airplane__capacity__gt=0  # traverse foreing key relations of Object-Relational Mapping (ORM)
        )
        serializer = self.get_serializer(available_reservations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        reservation = self.get_object()

        if not reservation.status:
            return Response(
                {"error": "Canceled reservations cannot be deleted."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        reservation.delete()
        return Response(
            {"message": "Reservation deleted successfully."}, status=status.HTTP_200_OK
        )

    def partial_update(self, request, *args, **kwargs):

        reservation = self.get_object()

        if not reservation.status:
            return Response(
                {"error": "Cannot update a canceled reservation."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().partial_update(request, *args, **kwargs)
