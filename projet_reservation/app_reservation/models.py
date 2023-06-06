from django.db import models
from django.db.models import ForeignKey
import random
from faker import Faker
from amadeus import Client, ResponseError
from django.utils import timezone

default_value = timezone.now()


amadeus = Client(
    client_id='RKx4s0hwYBfPWsEUx3JP3AAFxIuK4WRA',
    client_secret='pxrndHEwRQXNdTA9'
)
fake = Faker() 

class Utilisateur(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mot_de_passe = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)


def generer_numero():
    prefixe = random.choice(['70', '76', '77', '78'])
    numeros = ''.join(random.choice('0123456789') for _ in range(7))
    numero_telephone =prefixe + numeros
    return numero_telephone


class Compagnie(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    nom = models.CharField(max_length=255)



class Aeroport(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    nom = models.CharField(max_length=255)
    ville = models.CharField(max_length=255)
    code_ville = models.CharField(max_length=255)
    pays = models.CharField(max_length=255)
    code_pays = models.CharField(max_length=255)


class Vol(models.Model):
    compagnie = models.ForeignKey(Compagnie, to_field='code', on_delete=models.CASCADE, related_name='compagnie')
    aeroport_depart = models.ForeignKey(Aeroport, to_field='code', on_delete=models.CASCADE, related_name='vols_depart')
    aeroport_arrivee = models.ForeignKey(Aeroport, to_field='code', on_delete=models.CASCADE, related_name='vols_arrivee')
    date_depart = models.DateTimeField()
    date_arrivee = models.DateTimeField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_place = models.IntegerField()
    

class Hotel(models.Model):
    id_hotel = models.CharField(max_length=10, primary_key=True)
    nom = models.CharField(max_length=255)
    code_pays = models.CharField(max_length=255)


class Chambre(models.Model):
    hotel = models.ForeignKey(Hotel, to_field='id_hotel', on_delete=models.CASCADE, related_name='hotel')
    type_chambre= models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_place = models.DecimalField(max_digits=10, decimal_places=2)
    photo= models.CharField(max_length=255)

def choix_aleatoire(liste_mots):
    choix = random.choice(liste_mots)
    return choix


class Voiture(models.Model):
    marque= models.CharField(max_length=255)
    modele= models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    annee= models.IntegerField()
    type=models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_place =  models.IntegerField()
    photo= models.CharField(max_length=255)
    disponible=models.BooleanField(default=True)


class Reservation_Vol(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, to_field='id', on_delete=models.CASCADE, related_name='utilisateur')
    vol = models.ForeignKey(Vol, to_field='id', on_delete=models.CASCADE, related_name='vol')
    date = models.DateTimeField()


class Reservations_Hotel(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, to_field='id', on_delete=models.CASCADE, related_name='utilisateur2')
    chambre = models.ForeignKey(Chambre, to_field='id', on_delete=models.CASCADE, related_name='chambre')
    date_reservation = models.DateTimeField()
    date_restitution = models.DateTimeField()


class Location_Voiture(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, to_field='id', on_delete=models.CASCADE, related_name='utilisateur3')
    voiture = models.ForeignKey(Voiture, to_field='id', on_delete=models.CASCADE, related_name='voiture')
    date_reservation = models.DateTimeField()
    date_restitution = models.DateTimeField()

