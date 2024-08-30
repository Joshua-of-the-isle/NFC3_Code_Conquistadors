from django.shortcuts import render, get_object_or_404,redirect
from .models import PetShelter, Pet, PetAdoptionRequest
from .filters import PetFilter
from django.contrib.auth.decorators import login_required
from .decorators import group_required
from django.db.models import Count
from .forms import PetAdoptionRequestForm
def index(request):
    return render(request, 'pets/index.html')


# View to list all pet shelters
def shelter_list(request):
    shelters = PetShelter.objects.all()
    return render(request, 'pets/shelter_list.html', {'shelters': shelters})

# View to display details of a specific shelter
def shelter_detail(request, shelter_id):
    shelter = get_object_or_404(PetShelter, pk=shelter_id)
    return render(request, 'pets/shelter_detail.html', {'shelter': shelter})

def pet_list(request):
    pets = Pet.objects.all()
    initial_data = {'friendly': True} 
    pet_filter = PetFilter(request.GET or initial_data, queryset=pets)
    return render(request, 'pets/pet_list.html', {'filter': pet_filter})

# View to display details of a specific shelter
def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request, 'pets/pet_detail.html', {'pet': pet})


@login_required
@group_required('Shelter Owner')  # Replace 'ShelterManagers' with the desired group name
def shelter_dashboard(request):
    # Get the shelter associated with the logged-in user
    shelter = get_object_or_404(PetShelter, owner=request.user)
    
    # Get all pets associated with this shelter
    pets = Pet.objects.filter(shelter=shelter)
    
    # Calculate statistics
    total_pets = pets.count()
    pet_types = pets.values('pet_type').annotate(count=Count('id'))
    gender_distribution = pets.values('gender').annotate(count=Count('id'))
    adoption_status = pets.values('adopted').annotate(count=Count('id'))
    friendly_count = pets.filter(friendly=True).count()
    allergen_count = pets.filter(allergen=True).count()
    age_distribution = pets.values('age').annotate(count=Count('id'))

    # Prepare context data
    context = {
        'shelter': shelter,
        'total_pets': total_pets,
        'pet_types': list(pet_types),
        'gender_distribution': list(gender_distribution),
        'adoption_status': list(adoption_status),
        'friendly_count': friendly_count,
        'allergen_count': allergen_count,
        'age_distribution': list(age_distribution),
    }

    return render(request, 'pets/shelter_dashboard.html', context)

def pet_list_private(request):
    # Fetch all pet objects from the database
    pets = Pet.objects.filter(shelter=request.user.shelters.all()[0])
    return render(request, 'pets/pet_list.html', {'pets': pets})


@login_required
def adopt_pet(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    if request.method == 'POST':
        form = PetAdoptionRequestForm(request.POST)
        if form.is_valid():
            adoption_request = form.save(commit=False)
            adoption_request.pet = pet
            adoption_request.shelter = pet.shelter
            adoption_request.user = request.user
            adoption_request.save()
            return redirect(adoption_request.get_absolute_url())
    else:
        form = PetAdoptionRequestForm(initial={'comments': ''})
    
    return render(request, 'adopt_pet.html', {'form': form, 'pet': pet})


@login_required
@group_required('Shelter Owner')
def adoption_request_detail(request, pk):
    adoption_request = get_object_or_404(PetAdoptionRequest, pk=pk)
    return render(request, 'adoption_request_detail.html', {'adoption_request': adoption_request})

@login_required
@group_required('Shelter Owner')
def update_adoption_request_status(request, pk, status):
    adoption_request = get_object_or_404(PetAdoptionRequest, pk=pk)
    if request.user == adoption_request.shelter.owner:
        adoption_request.status = status
        adoption_request.save()
        adoption_request.send_email_notification()
    return redirect(adoption_request.get_absolute_url())