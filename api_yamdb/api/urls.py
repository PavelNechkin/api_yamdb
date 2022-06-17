from django.urls import include, path
# from rest_framework import routers

app_name = 'api'


urlpatterns = [
    # path('v1/', include(router_for_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]