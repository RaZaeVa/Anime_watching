from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView
from .views import *


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('list/', UserListAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]