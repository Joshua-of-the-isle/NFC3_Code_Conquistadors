# Generated by Django 5.1 on 2024-08-29 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_alter_pet_pet_type_petdonationrequest_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='adopted',
            new_name='under_adoption',
        ),
    ]
