from rest_framework import status
from rest_framework.response import Response

from address.models import Address

from address.serializer import AddressSerializer

from rest_framework.views import APIView
from variables.zipcodes import get_city_details, is_valid_zipcode
from .generic import CustomAPIView


class AddressAPIView(CustomAPIView):
    Model = Address
    queryset = Model.objects.all()
    serializer_class = AddressSerializer



class ZipCodeVIEW(APIView):

    def get(self, request, zipcode, *args, **kwargs):
        is_valid = is_valid_zipcode(zipcode)
        if is_valid: # check whether the zipcode in valid or not
            zipcode_data = get_city_details(zipcode)
            city_data = {
                **zipcode_data
            }
            result = {'status': status.HTTP_200_OK, "data": city_data}
        else:
            result = {'status': status.HTTP_404_NOT_FOUND,  "data": {}}
        return Response(**result)