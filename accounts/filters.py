import django_filters
from .models import Box
from django_filters.widgets import LinkWidget


class BoxFilters(django_filters.FilterSet):
    From = django_filters.CharFilter(label="Звідки")
    To = django_filters.CharFilter(label="Куди")
    class Meta:
        model = Box
        fields = ('From', 'To')
