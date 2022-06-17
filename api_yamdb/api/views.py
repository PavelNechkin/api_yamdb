from rest_framework import viewsets

from .serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
)
from reviews.models import (
    Category,
    Genre,
    Title,
)


class CategoryViewSet(viewsets.ModelViewSet):
    gueryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ModelViewSet):
    gueryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    gueryset = Title.objects.all()
    serializer_class = TitleSerializer
