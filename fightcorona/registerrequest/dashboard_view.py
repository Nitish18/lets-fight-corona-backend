import logging
import json
from rest_framework.views import APIView
from registerrequest.models import PeopleRequest, RequestDetail
from registerrequest.serializers import PeopleRequestSerializer, RequestDetailSerializer
from rest_framework.response import Response
from django.db.models import Count
from registerrequest.helpers import transform_response

logger = logging.getLogger(__name__)


class RequestDashboardView(APIView):
    def get(self, request):
        try:
            group_by_field = request.GET.get('group_by_field')
            if group_by_field:
                res = PeopleRequest.objects.values(group_by_field).annotate(Count('id'))
                res = transform_response(list(res), group_by_field=group_by_field)
                return Response({
                    "data": res
                },status=200)
            return Response({
                "status": "error",
                "reason": "no group by field provided",
            }, status=400)

        except Exception as e:
            logger.error("some error occurred - {}".format(str(e)))
            return Response({
                "status": "error",
                "reason": str(e)
            }, status=400)
