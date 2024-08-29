from django.shortcuts import render
from .models import PetItem
from .filters import PetItemFilter

def pet_item_list(request):
    pet_items = PetItem.objects.all()
    filterset = PetItemFilter(request.GET, queryset=pet_items)  # Apply filter

    context = {
        'filterset': filterset,  # Filtered queryset
    }
    return render(request, 'shop/pet_item_list.html', context)

