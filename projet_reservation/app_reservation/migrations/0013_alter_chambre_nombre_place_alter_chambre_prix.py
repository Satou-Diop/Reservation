# Generated by Django 4.2.1 on 2023-05-29 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_reservation", "0012_hotel_ville"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chambre",
            name="nombre_place",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="chambre",
            name="prix",
            field=models.IntegerField(),
        ),
    ]
