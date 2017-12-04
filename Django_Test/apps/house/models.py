from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator

class House(models.Model):
    TYPE_OF_HOME_CHOICES = (
        ("beach", "Beach"),
        ("bungalow", "Bungalow"),
        ("colonial", "Colonial"),
        ("contemporary", "Contemporary"),
        ("contemporary-craftsman", "Contemporary Craftsman"),
        ("country", "Country"),
        ("english-cottage", "English Cottage"),
        ("modern", "Modern"),
    )

    bedrooms = models.DecimalField(max_digits=2, decimal_places=1, unique=False, default=None)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, unique=False, default=None)
    floors = models.IntegerField(unique=False, default=1)
    paint_color = models.CharField(max_length=128,unique=False, default=None)
    style = models.CharField(max_length=128, unique=False, default="contemporary", choices=TYPE_OF_HOME_CHOICES)
    garage = models.CharField(max_length=3,default="N", choices=(("Y","Yes"),("N","No")))

    address_1 = models.CharField(max_length=128, default=None)
    address_2 = models.CharField(max_length=128, blank=True)

    city = models.CharField(max_length=64, default="Mishawaka")
    state = models.CharField(max_length=2, default="IN")
    zip_code = models.CharField(max_length=5, default="46544")

    class Meta:
        db_table = "house"
        verbose_name = "House"
        verbose_name_plural = "Houses"
        unique_together = (("address_1", "address_2", "city", "state", "zip_code"),) # Once again I just like composite keys as an enforcement tool

    def __str__(self):
        return self.color + " " + self.make + " " + self.model + " " + self.vehicle_type

    def get_composite_address(self):
        return self.address_1 + " " + self.address_2 + " " + self.city + ", " + self.state + " " + self.zip_code
