"""Миксины для тестов"""
from jwt_auth.tests.test_env import AUTH_HEADER_TYPES, LOGIN_URL
from rest_framework.response import Response
from rest_framework.test import APIClient


class ObtainTokensMixin:
    """Получает пару jwt-токенов"""
    @staticmethod
    def obtain_tokens(client: APIClient, credentials: dict) -> Response:
        response = client.post(LOGIN_URL, credentials, format='json')
        return response


class JWTAuthenticationMixin(ObtainTokensMixin):
    """
    Использует ObtainTokenMixin для получения пары jwt-токенов
    и записывает access-токен в header клиента для авторизации
    по данному токену.
    """
    def jwt_authenticate(self, client: APIClient, credentials: dict) -> None:
        response = self.obtain_tokens(client, credentials)
        access_token = response.data.get('access')
        client.credentials(
            HTTP_AUTHORIZATION=f'{AUTH_HEADER_TYPES[0]} {access_token}'
        )


class GetRefreshTokenMixin(ObtainTokensMixin):
    """
    Использует ObtainTokenMixin для получения пары jwt-токенов
    и возращает refresh-токен из указанной пары.
    """
    def get_refresh_token(self, client: APIClient, credentials: dict) -> str:
        login_response = self.obtain_tokens(client, credentials)
        return login_response.data.get('refresh')
