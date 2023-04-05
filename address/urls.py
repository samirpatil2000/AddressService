from django.urls import path
from .views import create_address, list_address
from address.api_views import AddressAPIView, ZipCodeVIEW, lat_logs, lat_log_single

urlpatterns = [
    # HTTP WEB
    path("add-address/", create_address, name="add_address"),
    path("address/", list_address, name="address"),

    # REST
    path("api/zipcodes/<str:zipcode>", ZipCodeVIEW.as_view()),
    path("api/address/", AddressAPIView.as_view()),
    path("api/latlongs", lat_logs),
    path("api/latlongs/<int:request_id>", lat_log_single),
    
]
