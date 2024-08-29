from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse# Define the PetShelter model
class PetShelter(models.Model):
    id=models.BigAutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shelters')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('pet_shelter_detail', args=[str(self.id)])

# Define the Pet model
class Pet(models.Model):
    PET_TYPES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
        ('Rabbit', 'Rabbit'),
        ('Other', 'Other'),
    ]
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    pet_type = models.CharField(max_length=10, choices=PET_TYPES)
    age = models.IntegerField()
    description = models.TextField()
    arrival_date = models.DateField(auto_now_add=True)
    adopted = models.BooleanField(default=False)
    # ForeignKey relationship to PetShelter
    shelter = models.ForeignKey(PetShelter, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pets-images/', blank=True, null=True)

    class Meta:
        ordering = ('-arrival_date',)
    def __str__(self):
        return f"{self.name} ({self.pet_type})"
    
    def get_absolute_url(self):
        return reverse('pet_shelter_detail', args=[str(self.id)])

