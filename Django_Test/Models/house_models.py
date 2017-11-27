from django.conf import settings
from django.db import models
from django.contrib.localflavor.us.models import USStateField

class House(models.Model):
    bedrooms = models.DecimalField(max_digits=2, decimal_places=1, unique=False, default=None)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, unique=False, default=None)
    floors = models.IntegerField(unique=False, default=1)
    paint_color = models.TextField(unique=False, default=None)
    style = models.TextField(unique=False, default="Contemporary")
    garage = models.BooleanField(default=False)

    address_1 = models.CharField(max_length=128, default=None)
    address_2 = models.CharField(max_length=128, blank=True)

    city = models.CharField(max_length=64, default="Mishawaka")
    state = USStateField(default="IN")
    zip_code = models.CharField(max_length=5, default="46544")

    class Meta:
        db_table = "house"
        verbose_name = "House"
        verbose_name_plural = "Houses"
        unique_together = (("address_1", "address_2", "city", "state", "zip_code"),) # Once again I just like composite keys as an enforcement tool

    def __str__(self):
        return str(self.year) + " " + self.color + " " + self.make + " " + self.model + " " + self.vehicle_type

    def get_composite_address(self):
        return self.address_1 + " " + self.address_2 + " " + self.city + ", " + self.state + " " + self.zip_code

    @staticmethod
    def basic_search_list():
        return [
            "serial_number", "make", "model", "color"
        ]
