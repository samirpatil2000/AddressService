from rest_framework import serializers
from .models import Address, LatLong


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = "__all__"

class LatLongSerializer(serializers.ModelSerializer):

    class Meta:
        model = LatLong
        fields = ['latitude', 'longitude', 'request_id']
