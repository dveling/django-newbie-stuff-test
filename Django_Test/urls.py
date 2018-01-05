"""Django_Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Django_Test.apps.house.views.class_based.HouseViews import HouseListView, HouseUpdateView, HouseCreateView, HouseDeleteView
from Django_Test.apps.person.views.class_based.PersonViews import PersonListView, PersonUpdateView, PersonCreateView, PersonDeleteView
from Django_Test.apps.vehicle.views.class_based.VehicleViews import VehicleListView, VehicleUpdateView, VehicleCreateView, VehicleDeleteView
from Django_Test.apps.base.baseviews.class_based.home import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^houses/$', HouseListView.as_view(), name='house-view-list'),
    url(r'^houses/view/(?P<pk>\d+)/$', HouseUpdateView.as_view(), name='house-details'),
    url(r'^houses/create/$', HouseCreateView.as_view(), name='house-create'),
    url(r'^houses/delete/(?P<pk>\d+)/$', HouseDeleteView.as_view(), name='house-delete'),
    url(r'^people/$', PersonListView.as_view(), name='person-view-list'),
    url(r'^people/view/(?P<pk>\d+)/$', PersonUpdateView.as_view(), name='person-details'),
    url(r'^people/create/$', PersonCreateView.as_view(), name='person-create'),
    url(r'^people/delete/(?P<pk>\d+)/$', PersonDeleteView.as_view(), name='person-delete'),
    url(r'^vehicles/$', VehicleListView.as_view(), name='vehicle-view-list'),
    url(r'^vehicles/view/(?P<pk>\d+)/$', VehicleUpdateView.as_view(), name='vehicle-details'),
    url(r'^vehicles/create/$', VehicleCreateView.as_view(), name='vehicle-create'),
    url(r'^vehicles/delete/(?P<pk>\d+)/$', VehicleDeleteView.as_view(), name='vehicle-delete'),
    url(r'^$', HomeView.as_view(), name='home')
]
