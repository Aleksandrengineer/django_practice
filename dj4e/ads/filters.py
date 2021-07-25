import django_filters
from .models import Ad


class AdFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Сначала новые'),
        ('descending', 'Сначала старые')
    )
    

    ordering = django_filters.ChoiceFilter(label='Сортировка по дате', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Ad
        fields = {
            'title':['icontains'],
            
        }

    def filter_by_order(self, queryset, name, value):
        expression = 'created_at' if value == 'ascending' else '-created_at'
        return queryset.order_by(expression)


