from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from Django_Test.apps.person.models import Person
import os
from Django_Test.settings import APPS_DIR
from django.core import serializers
from django.urls import reverse_lazy
from django.urls import reverse


class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'
    template_name = os.path.join(APPS_DIR, "person/templates/edit.html")
    success_url = '/person/'

class PersonDeleteView(DeleteView):
    model = Person
    success_url = '/person/'

class PersonListView(ListView):
    model = Person
    template_name = os.path.join(APPS_DIR, "person/templates/browse.html")

    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)
        is_deleting = self.request.GET.get("is_deleting", 0)
        context["is_deleting"] = is_deleting
        return context

class PersonUpdateView(UpdateView):
    model = Person
    fields = '__all__'
    template_name = os.path.join(APPS_DIR, "person/templates/details.html")
    success_url = '/person/'
