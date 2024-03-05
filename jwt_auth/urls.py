from django.urls import path

from jwt_auth.views import (CustomTokenObtainPairView, CustomTokenRefreshView,
                            LogoutViewJWT, UserDetail)

app_name = 'jwt_auth'

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh-token/', CustomTokenRefreshView.as_view(),
         name='refresh-token'),
    path('me/', UserDetail.as_view(), name='user-info'),
    path('logout/', LogoutViewJWT.as_view(), name='logout'),
]
