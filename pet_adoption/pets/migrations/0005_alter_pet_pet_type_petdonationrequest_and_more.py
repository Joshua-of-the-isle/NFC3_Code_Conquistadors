# Generated by Django 5.1 on 2024-08-29 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_alter_pet_gender_petadoptionrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_type',
            field=models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Bird', 'Bird'), ('Other', 'Other')], max_length=10),
        ),
        migrations.CreateModel(
            name='PetDonationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_type', models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Bird', 'Bird'), ('Other', 'Other')], max_length=10)),
                ('breed', models.CharField(default='Unknown', max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unknown', 'Unknown'), ('Unsexed', 'Unsexed')], max_length=10)),
                ('allergen', models.BooleanField(default=False)),
                ('friendly', models.BooleanField(default=True)),
                ('age', models.IntegerField()),
                ('description', models.TextField()),
                ('shelter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pets.petshelter')),
            ],
        ),
        migrations.DeleteModel(
            name='PetAdoptionRequest',
        ),
    ]
