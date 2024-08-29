from django.urls import path
from . import views
urlpatterns = [
    path('shelters/', views.shelter_list, name='shelter_list'),  # List of pet shelters
    path('shelters/<int:shelter_id>/',views.shelter_detail, name='shelter_detail'),  # Detail view of a pet shelter
    path('pets/', views.pet_list, name='pet_list'),  # List of pets
    path('pets/<int:pet_id>/', views.pet_detail, name='pet_detail'),  # Detail view of a pet
]