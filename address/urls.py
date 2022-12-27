from django.urls import path
from .views import create_address
from .api_views import AddressVIEW

urlpatterns = [
    # HTTP WEB
    path("add-address/", create_address, name="address"),

    # REST
    path("api/zipcodes/<str:zipcode>", AddressVIEW.as_view()),
]
