# Generated by Django 4.2.1 on 2023-06-07 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_reservation', '0011_location_voiture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vol',
            name='compagnie',
        ),
        migrations.RemoveField(
            model_name='vol',
            name='nombre_place',
        ),
        migrations.RemoveField(
            model_name='vol',
            name='prix',
        ),
    ]
