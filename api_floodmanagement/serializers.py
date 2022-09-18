
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
    image = serializers.ImageField()
    class Meta:
        model = CrowdSource
        fields = ['id', 'created_at' , 'latitude', 'longitude', 'category' , 'image' , 'description','owner'  ]
        
class ForcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForcastData
        fields = ['id', 'Site_Name' , 'River', 'State', 'District' , 'Day1' ,'Flood_Condition1' ,'Max_WL1'
                  , 'Day2' ,'Flood_Condition2' ,'Max_WL2', 'Day3' ,'Flood_Condition3' ,'Max_WL3'
                  , 'Day4' ,'Flood_Condition4' ,'Max_WL4', 'Day5' ,'Flood_Condition5' ,'Max_WL5' ]


class MapForcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloodForcastMap
        fields = ['id', 'Site_Name' , 'River', 'State', 'District' , 'Day1' ,'Flood_Condition1' ,'latitude', 'longitude' ]

class TipsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Tips
        fields = ['id','tips_category', 'image' ]


class SafeCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaftyCheck
        fields = ['latitude','longitude']


class InundationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrowdSource
        fields = ['latitude','longitude']



class MsgBroadcastSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MsgBroadcast
        fields = ['id','created_at', 'msg' ]