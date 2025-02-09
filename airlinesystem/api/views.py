from django.shortcuts import render
from rest_framework import viewsets
from .models import Airplane, Flight, Reservation
from .serializers import AirplaneSerializer, FlightSerializer, ReservationSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


class AirplaneView(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

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

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

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
    query_set = Reservation.objects.all()

    def list(self, response):
        serializer_class = ReservationSerializer(self.query_set, many=True)
        return Response(serializer_class)
