from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Product


class ProductFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='added_at',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
        }