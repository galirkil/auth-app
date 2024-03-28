from django.urls import path

from jwt_auth.views import (CustomTokenObtainPairView, CustomTokenRefreshView,
                            LogoutViewJWT, UserDetail, UserSignUpView)

app_name = 'jwt_auth'

urlpatterns = [
    path('register/', UserSignUpView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh-token/', CustomTokenRefreshView.as_view(),
         name='refresh-token'),
    path('me/', UserDetail.as_view(), name='user-info'),
    path('logout/', LogoutViewJWT.as_view(), name='logout'),
]
