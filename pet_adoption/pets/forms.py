# forms.py
from django import forms
from .models import PetShelter, Pet, PetAdoptionRequest

class PetAdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = PetAdoptionRequest
        fields = ['comments']
        widgets = {
            'comments': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        pet = kwargs.pop('pet', None)
        shelter = kwargs.pop('shelter', None)
        super().__init__(*args, **kwargs)
        if pet:
            self.fields['pet'].initial = pet
            self.fields['shelter'].initial = shelter

