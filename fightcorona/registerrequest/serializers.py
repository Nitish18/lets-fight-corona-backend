from registerrequest.models import RequestDetail, PeopleRequest
from rest_framework import serializers


class PeopleRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleRequest
        exclude = []

class RequestDetailSerializer(serializers.ModelSerializer):

    request = PeopleRequestSerializer()

    class Meta:
        model = RequestDetail
        exclude = []
