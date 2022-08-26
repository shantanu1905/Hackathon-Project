from django.shortcuts import render , HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView, )
from api_floodmanagement.models import *
from api_floodmanagement.serializers import HelpSerializer , CrowdSourceSerializer , ForcastSerializer , MapForcastSerializer , TipsSerializer , SafeCheckSerializer , InundationSerializer
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
#import geopy # used for extracting longitude and latitude from location name
import pandas as pd
import geopy.distance


class HelpList(ListCreateAPIView):
# With this endpoint we can do GET AND POST request to GET USER data who are requesting for HELP and USER can also POST their data .
    queryset = UserHelpRequest.objects.all()
    serializer_class = HelpSerializer
    permission_classes = [IsAuthenticated,  ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HelpDetail(RetrieveUpdateDestroyAPIView):
    # With this endpoint we can perform PUT , DELETE , requests
    permission_classes = [IsAuthenticated]
    serializer_class = HelpSerializer

    def get_queryset(self):
        # we will filter data on basis of current user 
        return UserHelpRequest.objects.all().filter(owner=self.request.user)
        
class HelpAllList(ListCreateAPIView):
    # With this endpoint we can perform GET methode to get only loged in user data
    permission_classes = [IsAuthenticated]
    serializer_class = HelpSerializer

    def get_queryset(self):
        # we will filter data on basis of current user 
        return UserHelpRequest.objects.all().filter(owner=self.request.user)


class CrowdSourceList(ListCreateAPIView):
# With this endpoint we can do GET AND POST request to GET Crowdsource data and POST crowdsource data .
    queryset = CrowdSource.objects.all()
    serializer_class = CrowdSourceSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['State', 'District' , 'created_at' ]
    filter_backends = (filters.SearchFilter,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        #print(serializer.data)




class CrowdSourceDetails(RetrieveUpdateDestroyAPIView):
    # With this endpoint we can perform PUT , DELETE , requests
    permission_classes = [IsAuthenticated]
    serializer_class = CrowdSourceSerializer

    def get_queryset(self):
        # we will filter data on basis of current user 
        return CrowdSource.objects.all().filter(owner=self.request.user)


class CrowdSourceListView(ListCreateAPIView):
    # With this endpoint we can perform GET methode to get only loged in user data
    permission_classes = [IsAuthenticated]
    serializer_class = CrowdSourceSerializer

    def get_queryset(self):
        # we will filter data on basis of current user 
        return CrowdSource.objects.all().filter(owner=self.request.user)


class ForcastList(ListCreateAPIView):
# With this endpoint we can do GET AND POST request to GET Crowdsource data and POST crowdsource data .
    
    search_fields = ['State', 'District' ]
    filter_backends = (filters.SearchFilter,)
    queryset = ForcastData.objects.all()
    serializer_class = ForcastSerializer
    #filter_backends=[DjangoFilterBackend]
    #filterset_fields=['State']
    permission_classes = []


class ForcastMapList(ListCreateAPIView):
# With this endpoint we can do GET AND POST request to GET Crowdsource data and POST crowdsource data .
    search_fields = ['State', 'District' ]
    filter_backends = (filters.SearchFilter,)
    queryset = FloodForcastMap.objects.all()
    serializer_class = MapForcastSerializer
    permission_classes = []

class Tips(ListCreateAPIView):
# With this endpoint we can do GET request to GET Tips data .
    search_fields = ['tips_category' ]
    filter_backends = (filters.SearchFilter,)
    queryset = Tips.objects.all()
    serializer_class = TipsSerializer
    permission_classes = []


class saftycheck(ListCreateAPIView ):
    queryset = SaftyCheck.objects.all()
    serializer_class = SafeCheckSerializer
    
    
    
    
    
    
def calculatedistance(request):
    dataset = FloodDataSet.objects.all()
    df = pd.DataFrame(list(FloodDataSet.objects.all().values()))
    df2 = SaftyCheck.objects.values().get(pk=1)
    chord2 = (df2["latitude"] , df2["longitude"])
    print(chord2)
    #print(df)
    longitude = df["longitude"].tolist()
    latitude = df["latitude"].tolist()
    
    distance = []
    for i , j, k in zip(latitude , longitude,df["Site_Name"].tolist() ):
       #distance.append(geopy.distance.geodesic((i,j) , chord2).km)
       distance.append({"Site_Name":k,"distance":geopy.distance.geodesic((i,j) , chord2).km})
    
    # print(distance.sort())

    i = 0
    shortest = distance[i]["distance"]
    shortest_station = distance[i]
    
    for i in range(len(distance)-1):
        if(shortest>distance[i+1]["distance"] ):
            shortest = distance[i+1]["distance"]
            shortest_station  = distance[i+1]
    
    print("shortest",shortest_station)


    new_water_level =pd.DataFrame(list(ForcastData.objects.filter(Site_Name=shortest_station["Site_Name"]).values()))
    print("New water level :" + str(new_water_level["Max_WL1"][0]))

    old_water_level =pd.DataFrame(list(FloodDataSet.objects.filter(Site_Name=shortest_station["Site_Name"]).values()))
    print("Old water level :" + str(old_water_level["water_level"][0]))


    return HttpResponse("done")

    
class Inundation(ListCreateAPIView):
    queryset = FloodForcastMap.objects.all()
    serializer_class = InundationSerializer
    permission_classes = [IsAuthenticated , ]

    def get(self, request, format=None):
        data = CrowdSource.objects.all()     
        df = pd.DataFrame(list(CrowdSource.objects.all().values()))


        serializer = self.serializer_class(data, many=True)
        serialized_data = serializer.dat      
        return Response(serialized_data, status=status.HTTP_200_OK )    



    