from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from jwt_auth.models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']
