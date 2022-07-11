
from rest_framework import serializers
from api.models import User
from api_floodmanagement.models import *


class HelpSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True, default=serializers.CurrentUserDefault())
    RequestStatus = models.CharField()
    class Meta:
        model = UserHelpRequest
        fields = ['id', 'created_at' , 'updated_at' , 'latitude', 'longitude', 'TypeOfEmergency' ,'RequestStatus' ,'owner'  ]
        

class CrowdSourceSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = CrowdSource
        fields = ['id', 'created_at' , 'latitude', 'longitude', 'category' , 'image' ,'owner'  ]
        