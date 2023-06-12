# Generated by Django 4.2.1 on 2023-06-12 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_reservation", "0015_location_voiture_disponible"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="location_voiture",
            name="disponible",
        ),
        migrations.AddField(
            model_name="reservations_hotel",
            name="paiement",
            field=models.BooleanField(default=False),
        ),
    ]
