from django.shortcuts import render, get_object_or_404
from .models import PetShelter, Pet

# View to list all pet shelters
def shelter_list(request):
    shelters = PetShelter.objects.all()
    return render(request, 'shelter_list.html', {'shelters': shelters})

# View to display details of a specific shelter
def shelter_detail(request, shelter_id):
    shelter = get_object_or_404(PetShelter, pk=shelter_id)
    pets = shelter.pet_set.all() # Use the related_name 'pets' to access all pets in the shelter#-
    return render(request, 'shelter_detail.html', {'shelter': shelter, 'pets': pets})

# View to list all pets
def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pet_list.html', {'pets': pets})

# View to display details of a specific shelter
def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request, 'pet_detail.html', {'pet': pet})