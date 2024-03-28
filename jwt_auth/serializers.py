from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from jwt_auth.models import CustomUser


class UserProfileSerializer(ModelSerializer):
    """
    Информация о текущей учетной записи пользователя.
    """
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
                  'date_joined']


class UserSignUpSerializer(ModelSerializer):
    """
    Для регистрации нового пользователя.
    """
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']


# Дальше идут сериализаторы используемые только для генерации схемы OpenAPi

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class DetailCodeErrorSerializer(serializers.Serializer):
    detail = serializers.CharField()
    code = serializers.CharField()


class DetailErrorSerializer(serializers.Serializer):
    detail = serializers.CharField()
