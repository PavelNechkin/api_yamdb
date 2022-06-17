from rest_framework import routers
from django.urls import path, include

from api.views import UserViewSet, get_jwt_token, register

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('users', UserViewSet,
                   basename='user')
urlpatterns = [
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token'),
    path('v1/', include(router_v1.urls)),
]
