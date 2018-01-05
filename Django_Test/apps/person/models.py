from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator
from Django_Test.apps.vehicle.models import Vehicle
from Django_Test.apps.house.models import House

class Person(models.Model):
    SSN = models.TextField(unique=True, default=None, validators=[RegexValidator(regex='^\d{3}-\d{2}-\d{4}$', message='Must be in format ###-##-####', code='nomatch')])
    first_name = models.TextField(unique=False, default=None)
    middle_intital = models.CharField(max_length=1, unique=False, default=None)
    last_name = models.TextField(unique=False, default=None)
    date_of_birth = models.DateField(unique=False, default=None)
    home = models.ForeignKey(House, on_delete=models.PROTECT)
    vehicles = models.ManyToManyField(Vehicle)

    class Meta:
        db_table = "person"
        verbose_name = "Person"
        verbose_name_plural = "Persons"
        unique_together = (("first_name", "middle_intital", "last_name", "date_of_birth", "SSN"),) # Once again I just like composite keys as an enforcement tool

    def __str__(self):
        return str(self.first_name) + " " + str(self.middle_intital) + " " + str(self.last_name) + " " + str(self.date_of_birth)
