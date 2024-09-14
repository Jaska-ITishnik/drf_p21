from django.db.models import Count, IntegerChoices
from django.db.models.functions import Length
from django_filters import FilterSet, ChoiceFilter, NumberFilter, BooleanFilter

from apps.models import Product, User, Category


class ProductFilterSet(FilterSet):
    class Number(IntegerChoices):
        n1 = 3
        n2 = 7
        n3 = 10
        n4 = 15

    by_user_type = ChoiceFilter(method='get_type', choices=User.Type.choices)
    length = NumberFilter(method='get_by_len')
    only_with_image = BooleanFilter(method='get_by_image')
    by_day = ChoiceFilter(method='get_by_day', choices=Number.choices)

    class Meta:
        model = Product
        fields = 'category',

    def get_type(self, queryset, name, value):
        return queryset.filter(owner__type=value)

    def get_by_len(self, queryset, name, value):
        return queryset.annotate(name_len=Length('name')).filter(name_len=value)

    def get_by_image(self, queryset, name, value):
        if value:
            return queryset.filter(photo__isnull=(not value))
        return queryset

    def get_by_day(self, queryset, name, value):
        return queryset.order_by('-created_at')[:int(value)]


class CategoryFilterSet(FilterSet):
    by_product_count = NumberFilter(method='get_by_product_count')

    class Meta:
        model = Category
        fields = 'name',

    def get_by_product_count(self, queryset, name, value):
        return queryset.annotate(product_count=Count('product')).filter(product_count=value).values('id', 'name',
                                                                                                    'slug')
