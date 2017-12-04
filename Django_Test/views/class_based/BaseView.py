from django.views.generic import ListView
from Django_Test.apps.house.models import House

class HouseList(ListView):
    model = House
    template_name = "base.html"
