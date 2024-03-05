"""Константы для тестов """
from django.urls import reverse

from config.settings import SIMPLE_JWT

LOGIN_URL = reverse('jwt-auth:login')
AUTH_HEADER_TYPES = SIMPLE_JWT.get('AUTH_HEADER_TYPES')
LOGOUT_URL = reverse('jwt-auth:logout')
REFRESH_TOKEN_URL = reverse('jwt-auth:refresh-token')
USER_INFO_URL = reverse('jwt-auth:user-info')
