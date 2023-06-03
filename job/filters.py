import django_filters
from.models import job


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    descrition = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = job
        fields = '__all__'
        exclude = ['owner','published_at','image','salary','vacancy','slug']