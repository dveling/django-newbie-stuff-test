from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator

class Vehicle(models.Model):
    make = models.TextField(unique=False, default=None)
    model = models.TextField(unique=False, default=None)
    year = models.IntegerField(unique=False, default=None)
    color = models.TextField(unique=False, default=None)
    vehicle_type = models.TextField(unique=False, default=None)
    serial_number = models.IntegerField(primary_key=True, unique=True, default=None)

    class Meta:
        db_table = "vehicle"
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"
        unique_together = (("make", "model", "year", "color", "vehicle_type", "serial_number"),) # not really needed due to serial_number being a primary key and providing uniqueness, but I like composite keys (even though django dosn't support them)

    def __str__(self):
        return str(self.year) + " " + self.color + " " + self.make + " " + self.model + " " + self.vehicle_type
