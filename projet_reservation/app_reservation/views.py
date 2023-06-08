from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import Utilisateur
import mysql.connector as sql
from django.shortcuts import render, get_object_or_404
from .models import Vol
config = {
    'user': 'phpmyadmin',
    'password': 'Mbambe92',
    'host': 'localhost',
    'database': 'latyr',
}
# Établir une connexion à la base de données
conn = sql.connect(**config)
cursor = conn.cursor()
nom,prenom,email,telephone,adresse,mot_de_passe='','','','','',''
# Create your views here.
def index(request):
    # Definir les variables globales
    
    context = {
        'variable': 'Contenu dynamique'
    }
    # Effectuer des opérations
    
    # Renvoyer une réponse HTTP
    #return HttpResponse('Un texte pour tester')
    return render(request, 'index.html', context)

from django.shortcuts import render





def connexion(request):
    if request.method=="POST":
        message=''
        email = request.POST.get('email')
        mot_de_passe = request.POST.get('mot_de_passe')
        if(email!='' and mot_de_passe!=''): 
            try:
                message=''
                conn = sql.connect(**config)
                cursor = conn.cursor()
                requete="select * from app_reservation_utilisateur where email LIKE'{}' and mot_de_passe LIKE '{}'".format(email,mot_de_passe)
                cursor.execute(requete)
                res=tuple(cursor.fetchall())
                if res==():
                    message='Login ou mot de passe incorrect'
                    cursor.close()
                    conn.close()
                    return render(request, 'connexion.html', {'erreur_message': message})
                    
                else :
                    cursor.close()
                    conn.close()
                    return redirect('index')
            except Exception as e:
                print(str(e))  # Afficher l'erreur pour le débogage
                message='Login ou mot de passe incorrect'
                return render(request, 'connexion.html', {'erreur_message': message})
        
    # Effectuer des opérations
    
    # Renvoyer une réponse HTTP
    #return HttpResponse('Un texte pour tester')
    else:
        context = {
        'variable': 'Contenu dynamique'
        }
        return render(request, 'connexion.html', context)


def inscription(request):
    if request.method=="POST":
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        adresse = request.POST.get('adresse')
        mot_de_passe = request.POST.get('mot_de_passe')
        mot_de_passe2 =request.POST.get('mot_de_passe2')
        if mot_de_passe!=mot_de_passe2:
            return HttpResponse('Les mots de passe ne correspondent pas')
        try:
            requete="insert into app_reservation_utilisateur (id,nom,prenom,adresse,email,telephone,mot_de_passe) values (NULL,'{}','{}','{}','{}','{}','{}')".format(nom,prenom,adresse,email,telephone,mot_de_passe)
            cursor.execute(requete)
            cursor.close()
            conn.close()
            return redirect('connexion')  # Rediriger vers la page d'accueil après l'inscription réussie
        except Exception as e:
            print(str(e))  # Afficher l'erreur pour le débogage
            return render(request, 'inscription.html', {'error_message': 'erreur'})
        
    # Effectuer des opérations
    
    # Renvoyer une réponse HTTP
    #return HttpResponse('Un texte pour tester')
    else:
        context = {
        'variable': 'Contenu dynamique'
        }
        return render(request, 'inscription.html', context)

def resultat(request):
    # Récupérer des données depuis le modèle
    
    context = {
        'variable': 'Contenu dynamique'
    }
    # Effectuer des opérations
    
    # Renvoyer une réponse HTTP
    #return HttpResponse('Un texte pour tester')
    return render(request, 'resultat.html', context)

def resultatvol(request):
    departure = request.POST.get('departure', '')
    arrival = request.POST.get('arrival', '')
    departure_time = request.POST.get('departure_time', '')
    arrival_time = request.POST.get('arrival_time', '')
    nombre_place = request.POST.get('nombre_place', '')
    prix = request.POST.get('prix', '')
    compagnie = request.POST.get('compagnie', '')
    image=request.POST.get('image','')

    try:
        conn = sql.connect(**config)
        cursor = conn.cursor()
        requete = "SELECT * FROM `app_reservation_vol` WHERE aeroport_depart_id = %s AND aeroport_arrivee_id = %s AND date_depart >= %s AND date_arrivee >= %s;"
        cursor.execute(requete, (departure, arrival, departure_time, arrival_time))
        res = cursor.fetchall()

        

        if res == []:
            return render(request, 'flight/resultatvol.html', {})
        else:
            resultats = []
            keys = ['id', 'date_depart', 'date_arrivee', 'prix','nombre_place','image','aeroport_depart', 'aeroport_arrivee', 'compagnie']
            for row in res:
                result = dict(zip(keys, row))
                resultats.append(result)
            liste_vols = { result['id']:{ 
                    'date_depart': result['date_depart'],
                    'date_arrivee': result['date_arrivee'],
                    'aeroport_depart': result['aeroport_depart'],
                    'aeroport_arrivee': result['aeroport_arrivee'],
                    'nombre_place': result['nombre_place'],
                    'prix': result['prix'],
                    'image': result['image'],

                    'compagnie': result['compagnie']
                } for result in resultats
                }
           
            # for result in resultats:
            #     vol_id = result['id']
            #     liste_vols[vol_id] = {
            #         'date_depart': result['date_depart'],
            #         'date_arrivee': result['date_arrivee'],
            #         'aeroport_depart': result['aeroport_depart.nom_aeroport'],
            #         'aeroport_arrivee': result['aeroport_arrivee.nom_aeroport'],
            #         'nombre_place': result['nombre_place'],
            #         'prix': result['prix'],
            #         'compagnie': result['compagnie']
            #     }
            context = {'liste_vols': liste_vols}
            cursor.close()
            conn.close()

            return render(request, 'flight/resultatvol.html', context)

    except Exception as e:
        print(str(e))  # Afficher l'erreur pour le débogage
        message = 'Erreur route'
        return render(request, 'flight/resultatvol.html', {'liste_vols': []})

def reservation_vol(request):
    # Récupérer les données du formulaire
    nom = request.POST.get('nom')
    email = request.POST.get('email')
    num_vol = request.POST.get('num_vol')
    mode_paiement = request.POST.get('mode_paiement')

    # Définir le contexte
    context = {
        'nom': nom,
        'email': email,
        'num_vol': num_vol,
        'mode_paiement': mode_paiement
    }

    # Renvoyer la réponse avec le template et le contexte
    return render(request, 'flight/reservation.html', context)

def confirmation_vol(request):
    # Récupérer les données du formulaire
    nom = request.POST.get('nom')
    email = request.POST.get('email')

    # Définir le contexte
    context = {
        'nom': nom,
        'email': email
    }

    # Renvoyer la réponse avec le template et le contexte
    return render(request, 'flight/confirmation.html', context)
       


# def vol_details(request, vol_id):
#     vol = Vol.objects.get(id=vol_id)
#     return render(request, 'vol_details.html', {'vol': vol})


