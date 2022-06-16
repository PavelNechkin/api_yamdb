from rest_framework import routers
from django.urls import path, include

from api.views import UserViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('users', UserViewSet,
                   basename='user')
urlpatterns = [
    path('v1/', include(router_v1.urls)),
]