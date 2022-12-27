from django.urls import path
from .views import create_address
urlpatterns = [
    path("add-address/", create_address, name="address")
]
