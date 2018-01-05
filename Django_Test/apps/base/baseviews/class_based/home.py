from django.shortcuts import render_to_response
from django.template import RequestContext
from Django_Test.settings import APPS_DIR
from django.views.generic.base import TemplateView
import os

class HomeView(TemplateView):
    template_name = os.path.join(APPS_DIR, "base/templates/home.html")
