# Generated by Django 5.1 on 2024-08-29 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0009_petadoptionrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='under_adoption',
            new_name='adopted',
        ),
    ]
