# Create your models here.
from django.db import models

class PetItem(models.Model):
    ITEM_CATEGORIES = [
        ('Food', 'Food'),
        ('Toy', 'Toy'),
        ('Accessory', 'Accessory'),
        ('Grooming', 'Grooming'),
        ('Health', 'Health'),
        ('Other', 'Other'),
    ]

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=ITEM_CATEGORIES)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='pet-images/', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Pet Item'
        verbose_name_plural = 'Pet Items'

    def __str__(self):
        return f"{self.name} of ({self.category})"
