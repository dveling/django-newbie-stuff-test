from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from Django_Test.apps.vehicle.models import Vehicle
import os
from Django_Test.settings import APPS_DIR
from django.core import serializers
from django.urls import reverse_lazy
from django.urls import reverse


class VehicleCreateView(CreateView):
    model = Vehicle
    fields = '__all__'
    template_name = os.path.join(APPS_DIR, "vehicle/templates/edit.html")
    success_url = '/vehicles/'

class VehicleDeleteView(DeleteView):
    model = Vehicle
    success_url = '/vehicles/'

class VehicleListView(ListView):
    model = Vehicle
    template_name = os.path.join(APPS_DIR, "vehicle/templates/browse.html")

    def get_context_data(self, **kwargs):
        context = super(VehicleListView, self).get_context_data(**kwargs)
        is_deleting = self.request.GET.get("is_deleting", 0)
        context["is_deleting"] = is_deleting
        return context

class VehicleUpdateView(UpdateView):
    model = Vehicle
    fields = '__all__'
    template_name = os.path.join(APPS_DIR, "vehicle/templates/details.html")
    success_url = '/vehicles/'
