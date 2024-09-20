from rest_framework import serializers
from django.contrib.auth.models import User
from status.models import Status
#For showing the data in the StatusSerializer 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class StatusSerializer(serializers.ModelSerializer):
    #user = UserSerializer(many=False) #For One user
    class Meta:
        model = Status
        fields = ['id', 'text', 'created_at', 'image_link', 'user']
        #image_link