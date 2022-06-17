from django.urls import include, path
from rest_framework import routers

from .views import (
    CategoryViewSet,
    GenreViewSet,
    TitleViewSet
)

app_name = 'api'


router_for_v1 = routers.DefaultRouter()
router_for_v1.register('categories', CategoryViewSet, basename='categories')
router_for_v1.register('genres', GenreViewSet, basename='genres')
router_for_v1.register('titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router_for_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
