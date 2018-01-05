from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from Django_Test.apps.house.models import House
import os
from Django_Test.settings import APPS_DIR
from django.core import serializers
from django.urls import reverse_lazy
from django.urls import reverse


class HouseCreateView(CreateView):
    model = House
    fields = '__all__'
    template_name = os.path.join(APPS_DIR, "house/templates/edit.html")
    success_url = '/houses/'

class HouseDeleteView(DeleteView):
    model = House
    success_url = '/houses/?is_deleting=1'

class HouseListView(ListView):
    model = House
    template_name = os.path.join(APPS_DIR, "house/templates/browse.html")

    def get_context_data(self, **kwargs):
        context = super(HouseListView, self).get_context_data(**kwargs)
        is_deleting = self.request.GET.get("is_deleting", 0)
        context["is_deleting"] = is_deleting
        return context

class HouseUpdateView(UpdateView):
    model = House
    fields = '__all__'
    template_name = os.path.join(APPS_DIR, "house/templates/details.html")
    success_url = '/houses/'
