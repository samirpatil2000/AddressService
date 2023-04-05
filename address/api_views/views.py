from rest_framework import status
from rest_framework.response import Response

from address.models import Address, LatLong

from address.serializer import AddressSerializer, LatLongSerializer

from rest_framework.views import APIView
from variables.zipcodes import get_city_details, is_valid_zipcode
from .generic import CustomAPIView


class AddressAPIView(CustomAPIView):
    Model = Address
    queryset = Model.objects.all()
    serializer_class = AddressSerializer



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def lat_logs(request):
    # if not request.user.is_authenticated:
    #     response = {"message": "User not authenticated"}
    #     return Response(response, status=status.HTTP_401_UNAUTHORIZED)
    if request.method == 'GET':
        latlong = LatLong.objects.filter()
        serializer = LatLongSerializer(latlong, many=True)
        response = {"message": "Data Loaded Successfully", "data": serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = LatLongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "Data Added Successfully"}
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {"message": "Invalid data"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def lat_log_single(request, request_id):
    # if not request.user.is_authenticated:
    #     response = {"message": "User not authenticated"}
    #     return Response(response, status=status.HTTP_401_UNAUTHORIZED)
    if request.method == 'GET':
        latlong = LatLong.objects.filter(request_id=request_id)
        serializer = LatLongSerializer(latlong, many=True)
        response = {"message": "Data Loaded Successfully", "data": serializer.data}
        return Response(response, status=status.HTTP_200_OK)



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