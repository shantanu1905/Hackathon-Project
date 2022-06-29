
from rest_framework import serializers
from api.models import User
from api_floodmanagement.models import *


class HelpSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True, default=serializers.CurrentUserDefault())
    RequestStatus = models.CharField()
    class Meta:
        model = UserHelpRequest
        fields = ['id', 'latitude', 'longitude','created', 'TypeOfEmergency' ,'owner' , 'RequestStatus']
        