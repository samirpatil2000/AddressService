from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class AddressVIEW(APIView):

    def get(self, request, *args, **kwargs):
        is_valid = True
        if is_valid: # check whether the zipcode in valid or not
            city_data = {
                "city": "Mumbai",
                "state": "Maharashtra"
            }
            result = {'status': status.HTTP_200_OK, 'message': "Successfully Loaded..!", "data": city_data}
        else:
            result = {'status': status.HTTP_200_OK, 'message': "Invalid Zipcode..!", "data": {}}
        return Response(result)