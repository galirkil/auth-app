from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_205_RESET_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from jwt_auth.serializers import (LogoutSerializer, UserProfileSerializer,
                                  UserSignUpSerializer)


@extend_schema(summary="Регистрация нового пользователя", auth=[])
class UserSignUpView(CreateAPIView):
    """
    Регистрация нового пользователя.

    Принимает email, username, password
    и создает нового пользователя с указанными данными.
    """
    serializer_class = UserSignUpSerializer


@extend_schema(summary="Получение пары jwt-токенов")
class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Принимает email-адрес пользователя и пароль, возвращает пару
    access и refresh jwt-токенов подтвреждающих аутентификацию пользователя.
    """
    pass


@extend_schema(summary="Обновление access-токена")
class CustomTokenRefreshView(TokenRefreshView):
    """
    Принимает refresh-токен и возращает access-токен, если refresh-токен
    действителен.
    """
    pass


class UserDetail(APIView):
    """
    Предоставляет информацию о текущей авторизованной
    учетной записи пользователя.
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Информация о текущем пользователе",
        responses={200: UserProfileSerializer}
    )
    def get(self, request: Request) -> Response:
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)


class LogoutViewJWT(APIView):
    """Завершает сессию текущего пользвателя путем добавления его
    reshresh-токена в черный список.
    """
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        summary="Завершение текущей сессии",
        auth=[],
        request=LogoutSerializer,
        responses={HTTP_205_RESET_CONTENT: OpenApiResponse()}
    )
    def post(self, request: Request) -> Response:
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=HTTP_205_RESET_CONTENT)
        except TokenError as bad_token:
            return Response(status=HTTP_400_BAD_REQUEST,
                            data={"detail": str(bad_token)})
