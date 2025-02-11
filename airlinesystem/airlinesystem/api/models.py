from django.db import models
import random
import string
from django.core.exceptions import ValidationError

# Create your models here.


class Airplane(models.Model):
    tail_number = models.CharField(max_length=6, unique=True, primary_key=True)
    model = models.CharField(max_length=50)
    capacity = models.IntegerField()
    production_year = models.IntegerField()
    status = models.BooleanField(default=True)
    # PROTECT couldb be used if Airplane is still used in a Flight.

    def __str__(self):
        return f"{self.model} ({self.tail_number})"


class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airplane = models.ForeignKey(
        Airplane,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="flights",
    )

    def __str__(self):
        return f" Flight {self.flight_number} ({self.departure} to {self.destination})"


class Reservation(models.Model):
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    reservation_code = models.CharField(max_length=10, unique=True, editable=False)
    flight = models.ForeignKey(
        Flight,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="reservations",
    )
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation {self.reservation_code} for {self.passenger_name}"

    def save(self, *args, **kwargs):

        if self.flight.reservations.count() > self.flight.airplane.capacity:
            raise ValidationError("This flight is fully booked.")

        if not self.reservation_code:
            self.reservation_code = self.generate_reservation_code()
        super().save(*args, **kwargs)

    def generate_reservation_code(self):

        characters = string.ascii_uppercase + string.digits
        code = "".join(random.choices(characters, k=6))

        while Reservation.objects.filter(reservation_code=code).exists():
            code = "".join(random.choices(characters, k=6))

        return code

    def __str__(self):
        return f"Reservation {self.reservation_code} for {self.passenger_name}"
