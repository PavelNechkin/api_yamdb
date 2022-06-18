from rest_framework import routers
from django.urls import path, include

from api.views import UserViewSet, get_jwt_token, register
from api.views import (
    CategoryViewSet,
    GenreViewSet,
    TitleViewSet
)
app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('users', UserViewSet,basename='user')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitleViewSet, basename='titles')
urlpatterns = [
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token'),
    path('v1/', include(router_v1.urls)),
]
