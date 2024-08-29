from django.contrib import admin
from .models import PetItem
# Register your models here.
@admin.register(PetItem)
class PetItemAdmin(admin.ModelAdmin):
    pass