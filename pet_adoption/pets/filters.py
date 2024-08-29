import django_filters
from django import forms
from .models import Pet

class PetFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'placeholder': 'Enter pet name'}),
        help_text='Filter pets by name (case-insensitive).'
    )
    pet_type = django_filters.ChoiceFilter(
        choices=Pet.PET_TYPES,
        widget=forms.Select,
        help_text='Filter pets by type.'
    )
    breed = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'placeholder': 'Enter breed'}),
        help_text='Filter pets by breed (case-insensitive).'
    )
    gender = django_filters.ChoiceFilter(
        choices=Pet.GENDER_CHOICES,
        widget=forms.Select,
        help_text='Filter pets by gender.'
    )
    allergen = django_filters.BooleanFilter(
        widget=forms.CheckboxInput,
        help_text='Filter pets that are hypoallergenic or not.'
    )
    friendly = django_filters.BooleanFilter(
        widget=forms.CheckboxInput,
        initial=True,
        help_text='Filter pets that are friendly or not.'
    )
    age = django_filters.NumberFilter(
        lookup_expr='gte',
        widget=forms.NumberInput(attrs={'min': '0', 'step': '1'}),
        help_text='Filter pets older than or equal to the specified age.'
    )
    adopted = django_filters.BooleanFilter(
        widget=forms.CheckboxInput,
        help_text='Filter pets by adoption status.'
    )

    class Meta:
        model = Pet
        fields = ['name', 'pet_type', 'breed', 'gender', 'allergen', 'friendly', 'age', 'adopted']
