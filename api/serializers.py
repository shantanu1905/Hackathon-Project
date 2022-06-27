from rest_framework import serializers
from api.models import User


class UserRegistrationView(serializers.ModelSerializer):
    # we are writing this becausewe need confirm password field in our registration request
    password2 = serializers.CharField(style={'input_type':'password' , 'write_only':True})
    class Meta:
        model=User
        field = ['email','name', 'password' , 'password2' , 'contact']
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