from django.urls import path
from .views import create_address, list_address
from .api_views import AddressVIEW

urlpatterns = [
    # HTTP WEB
    path("add-address/", create_address, name="add_address"),
    path("address/", list_address, name="address"),

    # REST
    path("api/zipcodes/<str:zipcode>", AddressVIEW.as_view()),
]
