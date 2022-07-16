
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView, )
from api_floodmanagement.models import *
from api_floodmanagement.serializers import HelpSerializer , CrowdSourceSerializer , ForcastSerializer
#from django_filters.rest_framework import DjangoFilterBackend

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
        


class CrowdSourceList(ListCreateAPIView):
# With this endpoint we can do GET AND POST request to GET Crowdsource data and POST crowdsource data .
    queryset = CrowdSource.objects.all()
    serializer_class = CrowdSourceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CrowdSourceDetails(RetrieveUpdateDestroyAPIView):
    # With this endpoint we can perform PUT , DELETE , requests
    permission_classes = [IsAuthenticated]
    serializer_class = CrowdSourceSerializer

    def get_queryset(self):
        # we will filter data on basis of current user 
        return CrowdSource.objects.all().filter(owner=self.request.user)


class ForcastList(ListCreateAPIView):
# With this endpoint we can do GET AND POST request to GET Crowdsource data and POST crowdsource data .
    serializer_class = ForcastSerializer
    queryset = ForcastData.objects.all()
    #filter_backends=[DjangoFilterBackend]
    filterset_fields=['State']
    permission_classes = []

    