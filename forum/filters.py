import django_filters
from django.db.models import Count

from forum.models import Topic


class TopicFilter(django_filters.FilterSet):
    date_span = django_filters.DateRangeFilter(field_name='created', label='Период создания')
    comments = django_filters.CharFilter(field_name='comment__content', lookup_expr='icontains', label='Комментарии')
    subject = django_filters.CharFilter(lookup_expr='icontains', label='Тема обсуждения')
    creator = django_filters.CharFilter(field_name='creator__username', lookup_expr='icontains', label='Создатель темы')
    is_empty = django_filters.BooleanFilter(method='filter_empty', label='Темы без комментариев')

    class Meta:
        model = Topic
        fields = ['subject', 'creator', 'date_span', 'comments', 'is_empty']

    def filter_empty(self, queryset, name, value):
        queryset = Topic.objects.annotate(comment_count=Count('comments'))

        if value is True:
            return queryset.filter(comment_count__lt=1)
        elif value is False:
            return queryset.filter(comment_count__gte=1)
        else:
            return queryset
