from dataclasses import field
from unittest.util import _MAX_LENGTH
from xml.dom import ValidationErr
from rest_framework import serializers
from api.models import User
from django.utils.http import  urlsafe_base64_decode , urlsafe_base64_encode
from django.utils.encoding import smart_bytes , smart_str , force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class UserRegistrationSerializer(serializers.ModelSerializer):
    # we are writing this becausewe need confirm password field in our registration request
    password2 = serializers.CharField(style={'input_type':'password' , 'write_only':True})
    class Meta:
        model=User
        fields = ['email','name', 'password' , 'password2' , 'contact']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    # from views data in comming into attrs atribute and by this function we will validate user password    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("password and Confirm password doesn't match")

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        model =User
        fields = ['email','password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name' , 'email' , 'contact' ]


class SendPasswordRestEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        field = ['email']

    def validate(self, attrs):
        email= attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid=urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded UID' , uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('password reset token' , token)
            link = 'http://localhost:8000/api/user/reset/'+uid+'/'+token
            print('link',link)
            return attrs

        else:
            raise serializers.ValidationError('you are not registered user')

    
