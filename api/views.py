
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer , UserLoginSerializer , UserProfileSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken

# Generate Token Mannauly
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

#Registration 
class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data) # data is send to serilizers
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token ,'msg' : 'Registration Success!'} , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request, format=None):
         serializer = UserLoginSerializer(data=request.data) # data is send to serilizers
         if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user=authenticate(email=email , password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({ 'token':token ,'msg' : 'Login Success!'} , status=status.HTTP_200_OK)
            else:
                return Response({'errors' : {'non_field_error':['Email or password is not valid']}} , status=status.HTTP_404_NOT_FOUND)

         return Response({'msg' : 'Login Success!'} , status=status.HTTP_200_OK)


class UserProfileView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)
