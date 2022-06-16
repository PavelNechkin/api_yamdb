from rest_framework import viewsets

from api.serializers import UserSerializer
from reviews.models import User


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
