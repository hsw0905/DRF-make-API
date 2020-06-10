import django_filters as filters
from .models import Snippet

class SnippetFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    starts_with_code = filters.CharFilter(field_name="code", method='filter_starts_with_code')
    ends_with_code = filters.CharFilter(field_name="code", method='filter_ends_with_code')

    def filter_starts_with_code(self, queryset, name, value):
        f = {f'{name}__startswith':value}
        return queryset.filter(**f)

    def filter_ends_with_code(self, queryset, name, value):
        f = {f'{name}__endswith':value}
        return queryset.filter(**f)

    class Meta:
        model = Snippet
        fields = ['price','min_price','max_price',]