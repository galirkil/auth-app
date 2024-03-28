from rest_framework import status
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken

from jwt_auth.tests.base_test_case import BaseApiTestCase
from jwt_auth.tests.test_env import (LOGOUT_URL, REFRESH_TOKEN_URL,
                                     USER_INFO_URL)
from jwt_auth.tests.test_mixins import (GetRefreshTokenMixin,
                                        JWTAuthenticationMixin,
                                        ObtainTokensMixin)


class CustomTokenObtainPairViewTests(BaseApiTestCase, ObtainTokensMixin):
    """Тестирует view получения пары jwt-токенов"""
    def test_user_can_obtain_tokens_with_valid_credentials(self):
        response = self.obtain_tokens(self.client, self.credentials)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_cant_obtain_tokens_with_invalid_credentials(self):
        credentials = {
            'email': self.credentials['email'] + 'not_valid',
            'password': self.credentials['password'] + 'not_valid'
        }
        response = self.obtain_tokens(self.client, credentials)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class CustomTokenRefreshViewTests(BaseApiTestCase, GetRefreshTokenMixin):
    """Тестирует view обновления access-токена"""
    def test_user_can_refresh_access_token(self):
        refresh_token = self.get_refresh_token(self.client, self.credentials)
        response = self.client.post(REFRESH_TOKEN_URL,
                                    {'refresh': refresh_token}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)


class UserDetailViewTests(BaseApiTestCase, JWTAuthenticationMixin):
    """Тестирует view получения информации о текущем пользователе"""
    def test_authorized_user_can_get_current_user_info(self):
        self.jwt_authenticate(self.client, self.credentials)
        response = self.client.get(USER_INFO_URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user_info['username'])
        self.assertEqual(response.data['email'], self.user_info['email'])

    def test_unauthorized_user_cant_get_current_user_info(self):
        response = self.client.get(USER_INFO_URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class LogoutViewJWTTests(BaseApiTestCase, GetRefreshTokenMixin):
    """Тестирует view завершения сессии текущего пользователя"""
    def test_user_can_logout(self):
        refresh_token = self.get_refresh_token(self.client, self.credentials)
        is_token_blacklisted = BlacklistedToken.objects.filter(
            token__token=refresh_token).exists()
        self.assertEqual(is_token_blacklisted, False)
        response = self.client.post(LOGOUT_URL, {'refresh': refresh_token},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
        is_token_blacklisted_after_request = BlacklistedToken.objects.filter(
            token__token=refresh_token).exists()
        self.assertEqual(is_token_blacklisted_after_request, True)
