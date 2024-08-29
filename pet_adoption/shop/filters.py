import django_filters
from .models import PetItem

class PetItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Name',
        help_text='Search by item name (e.g., "Dog Food")'
    )
    category = django_filters.ChoiceFilter(
        choices=PetItem.ITEM_CATEGORIES,
        empty_label='All Categories',
        label='Category',
        help_text='Select the category of the pet item'
    )
    min_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte',
        label='Min Price',
        help_text='Filter items with a price greater than or equal to this amount'
    )
    max_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte',
        label='Max Price',
        help_text='Filter items with a price less than or equal to this amount'
    )

    class Meta:
        model = PetItem
        fields = ['name', 'category', 'min_price', 'max_price']
