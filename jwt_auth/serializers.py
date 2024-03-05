from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from jwt_auth.models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class DetailCodeErrorSerializer(serializers.Serializer):
    detail = serializers.CharField()
    code = serializers.CharField()


class DetailErrorSerializer(serializers.Serializer):
    detail = serializers.CharField()
