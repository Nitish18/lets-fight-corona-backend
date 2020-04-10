import logging
import json
from rest_framework.views import APIView
from registerrequest.models import PeopleRequest, RequestDetail
from registerrequest.serializers import PeopleRequestSerializer, RequestDetailSerializer
from rest_framework.response import Response

logger = logging.getLogger(__name__)

class PeopleRequestView(APIView):
    def get(self, request):
        all_requests = PeopleRequest.objects.all()
        try:
            request_type = request.GET.get('request_type')
            if request_type:
                all_requests = all_requests.filter(request_type=request_type)

            request_status = request.GET.get('request_status')
            if request_status:
                all_requests = all_requests.filter(request_status=request_status)

            city = request.GET.get('city')
            if city:
                all_requests = all_requests.filter(city=city)

            pin_code = request.GET.get('pin_code')
            if pin_code:
                all_requests = all_requests.filter(pin_code=pin_code)

            all_request_serializer = PeopleRequestSerializer(all_requests, many=True)
            return Response(all_request_serializer.data, status=200)
        except Exception as e:
            logger.error("Some error occurred - {}".format(str(e)))
            return Response({
                "status": "error",
                "reason": str(e)
            }, status=400)

    def post(self, request):
        try:
            payload = request.data
            request_info = {
                'request_type': payload.get('request_type'),
                'name': payload.get('name'),
                'address': payload.get('address'),
                'pin_code': payload.get('pin_code'),
                'city': payload.get('city'),
                'phone_number': payload.get('phone_number'),
                'request_status': payload.get('request_status', "pending"),
            }
            request_meta_detail = {
                'no_of_people': payload.get('no_of_people'),
                'food_grocery_type': payload.get('food_grocery_type'),
                'food_grocery_type_detail': payload.get('food_grocery_type_detail'),
                'medicine_request_detail': payload.get('medicine_request_detail'),
                'feeling_sick': payload.get('feeling_sick'),
                'feeling_sick_detail': payload.get('feeling_sick_detail'),
            }

            # saving request entry in DB first.
            people_request_serializer = PeopleRequestSerializer(data=request_info)
            if people_request_serializer.is_valid():
                people_request_object = people_request_serializer.save()

                request_meta_detail['request'] = people_request_object.pk
                people_request_detail_seriaizer = RequestDetailSerializer(data=request_meta_detail)
                if people_request_detail_seriaizer.is_valid():
                    people_request_detail_object = people_request_detail_seriaizer.save()
                    logger.info("logged a request successfully - request id - {}, request detail id - {}".format(
                        people_request_object.pk,
                        people_request_detail_object.pk,
                    ))
                    return Response("logged a request successfully - request id - {}, request detail id - {}".format(
                        people_request_object.pk,
                        people_request_detail_object.pk,
                    ), status=201)
                else:
                    # some validation error - deleting parent request object as well.
                    PeopleRequest.objects.get(id=people_request_object.pk).delete()
            logger.error("some error occurred")
            return Response("some error occurred", status=400)
        except Exception as e:
            logger.error("Some error occurred - {}".format(str(e)))
            return Response({
                "status": "error",
                "reason": str(e)
            }, status=400)
