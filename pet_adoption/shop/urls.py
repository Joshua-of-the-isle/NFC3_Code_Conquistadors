from django.urls import path
from .views import pet_item_list

urlpatterns = [
    path('', pet_item_list, name='pet_item_list'),
]
