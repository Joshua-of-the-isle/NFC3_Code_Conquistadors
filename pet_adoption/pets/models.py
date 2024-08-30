from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse# Define the PetShelter model
from django.core.mail import send_mail
from django.conf import settings
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
        return reverse('shelter_detail', args=[str(self.id)])

# Define the Pet model
class Pet(models.Model):
    PET_TYPES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
        ('Other', 'Other'),
    ]
    GENDER_CHOICES=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Unknown', 'Unknown'),
        ('Unsexed', 'Unsexed'),
    ]
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    pet_type = models.CharField(max_length=10, choices=PET_TYPES)
    breed = models.CharField(max_length=50, default='Unknown')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    allergen=models.BooleanField(default=False)
    friendly=models.BooleanField(default=True)
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
        return reverse('pet_detail', args=[str(self.id)])

class PetAdoptionRequest(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='adoption_requests')
    shelter = models.ForeignKey(PetShelter, on_delete=models.CASCADE, related_name='adoption_requests')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adoption_requests')
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')],
        default='Pending'
    )
    comments = models.TextField()

    class Meta:
        ordering = ('-request_date',)

    def __str__(self):
        return f"{self.user.username}'s request for {self.pet.name}"

    def get_absolute_url(self):
        return reverse('adoption_request_detail', args=[str(self.id)])

    def send_email_notification(self):
        subject = f"Your adoption request for {self.pet.name} has been {self.status.lower()}"
        message = f"Dear {self.user.username},\n\nYour adoption request for {self.pet.name} has been {self.status.lower()}.\n\n{self.comments}\n\nThank you,\nPet Shelter"
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [self.user.email]
        )
