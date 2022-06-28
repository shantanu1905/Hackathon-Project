
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from api_floodmanagement.models import *

from rest_framework_simplejwt.tokens import RefreshToken


