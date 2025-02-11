from rest_framework import serializers
from .models import Airplane, Flight, Reservation


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = "__all__"


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"

    def validate(self, data):
        airplane = data.get("airplane")
        if airplane and not airplane.status:
            raise serializers.ValidationError(
                f"Cannot create flight. The airplane '{airplane.tail_number}' is not available."
            )
        return data


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"  # spesicially array can be defined
        read_only_fields = ("reservation_code",)
