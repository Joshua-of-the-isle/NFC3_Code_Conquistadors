from django.urls import path
from . import views
urlpatterns = [
    path('shelters/', views.shelter_list, name='shelter_list'),  # List of pet shelters
    path('shelters/<int:shelter_id>/',views.shelter_detail, name='shelter_detail'),  # Detail view of a pet shelter
    path('pets/', views.pet_list, name='pet_list'),  # List of pets
    path('pets/<int:pet_id>/', views.pet_detail, name='pet_detail'),  # Detail view of a pet
    path('shelters/dashboard/', views.shelter_dashboard, name='shelter_dashboard'),
    path('shelters/pets/', views.pet_list_private, name='pet_list_private'),
    path('pet/<int:pet_id>/adopt/', views.adopt_pet, name='adopt_pet'),
]