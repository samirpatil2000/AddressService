from django.urls import path
from .views import create_address, list_address
from address.api_views import AddressAPIView, ZipCodeVIEW

urlpatterns = [
    # HTTP WEB
    path("add-address/", create_address, name="add_address"),
    path("address/", list_address, name="address"),

    # REST
    path("api/zipcodes/<str:zipcode>", ZipCodeVIEW.as_view()),
    path("api/address/", AddressAPIView.as_view()),
    
]
