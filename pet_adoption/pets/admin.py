from django.contrib import admin
from .models import PetShelter, Pet
# Register your models here.

@admin.register(PetShelter)
class PetShelterAdmin(admin.ModelAdmin):
    pass

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass