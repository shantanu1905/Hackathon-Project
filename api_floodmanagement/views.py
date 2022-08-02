
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView, )
from api_floodmanagement.models import *
from api_floodmanagement.serializers import HelpSerializer , CrowdSourceSerializer , ForcastSerializer
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
#import geopy # used for extracting longitude and latitude from location name



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
    
    search_fields = ['State']
    filter_backends = (filters.SearchFilter,)
    queryset = ForcastData.objects.all()
    serializer_class = ForcastSerializer
    #filter_backends=[DjangoFilterBackend]
    #filterset_fields=['State']
    permission_classes = []
