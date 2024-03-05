from rest_framework.test import APITestCase

from jwt_auth.models import CustomUser
from jwt_auth.tests.test_credentials import UserDummy


class BaseApiTestCase(APITestCase):
    """Базовый класс для тестов содержит общий сетап"""

    def setUp(self) -> None:
        super().setUp()
        self.user_info: dict = UserDummy.get_user_info()
        self.user = CustomUser.objects.create_user(**self.user_info)
        self.credentials = {
            'email': self.user_info.get('email'),
            'password': self.user_info.get('password')
        }
