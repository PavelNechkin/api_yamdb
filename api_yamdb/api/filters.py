import django_filters as DJ

from reviews.models import Title


class FilterForTitle(DJ.FilterSet):
    category = DJ.CharFilter(field_name='category__slug')
    genre = DJ.CharFilter(field_name='genre__slug')
    name = DJ.CharFilter(field_name='name', lookup_expr='icontains')
    year = DJ.NumberFilter(field_name='year')

    class Meta:
        model = Title
        fields = '__all__'
