from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import Utilisateur
import mysql.connector as sql
from django.shortcuts import render, get_object_or_404
from .models import Vol
from django.core.mail import send_mail
from django.conf import settings
from app_reservation.models import Utilisateur
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



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
    submitted=False
    if request.method=="POST":
        message=''
        email = request.POST.get('email')
        mot_de_passe = request.POST.get('mot_de_passe')
        if(email!='' and mot_de_passe!=''): 
            try:
                message=''
                conn = sql.connect(**config)
                cursor = conn.cursor()
                requete="select * from app_reservation_utilisateur where  email='{}' and  BINARY  mot_de_passe='{}'".format(email,mot_de_passe)
                cursor.execute(requete)
                res=cursor.fetchall()
                if res==[]:
                    message='Login ou mot de passe incorrect'
                    cursor.close()
                    conn.close()
                    return render(request, 'connexion.html', {'erreur_message': message})
                    
                else :
                    keys = ['id', 'nom', 'prenom', 'adresse', 'email', 'telephone']
                    result = dict(zip(keys, res[0]))
                    result['estConnecte'] = True
                    cursor.close()
                    conn.close()
                    # Stocker le dictionnaire dans la session
                    request.session['info_utilisateur'] = result
                    return redirect('index')
                
            except Exception as e:
                print(str(e))  # Afficher l'erreur pour le débogage
                message='Erreur route'
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

        try:
            conn = sql.connect(**config)
            cursor = conn.cursor()
            requete="insert into app_reservation_utilisateur (id,nom,prenom,adresse,email,telephone,mot_de_passe) values (NULL,'{}','{}','{}','{}','{}','{}')".format(nom,prenom,adresse,email,telephone,mot_de_passe)
            cursor.execute(requete)
            conn.commit()
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
    if request.method == 'POST':
        # Traitement du formulaire et enregistrement de la réservation
        
        return render(request, 'flight/reservation.html')
    else:
        return render(request, 'flight/reservation.html')

def confirmation_vol(request):
    if request.method == 'POST':
        # Traitement du formulaire et enregistrement de la réservation
        
        # Envoyer l'e-mail de confirmation
        nom = request.POST['nom']
        email = request.POST['email']
        num_vol = request.POST['num_vol']
        
        sujet = 'Confirmation de réservation'
        message = f'Cher {nom},\n\nVotre réservation pour le vol {num_vol} a été confirmée. Merci de votre confiance !\n\nCordialement,\nVotre compagnie aérienne'
        destinataires = [email]
        
        send_mail(sujet, message, settings.DEFAULT_FROM_EMAIL, destinataires)

        return render(request, 'flight/confirmation.html', {'nom': nom, 'email': email, 'num_vol': num_vol})
    else:
        return render(request, 'flight/reservation.html')
      
       


# def vol_details(request, vol_id):
#     vol = Vol.objects.get(id=vol_id)
#     return render(request, 'vol_details.html', {'vol': vol})


def mes_reservations(request):
    
    if 'info_utilisateur' in request.session:
        info_utilisateur = request.session['info_utilisateur']
        if 'id' in info_utilisateur:
            id_user = info_utilisateur['id']
    try:
        conn = sql.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `app_reservation_reservations_vol` where utilisateur_id ='{}' ".format(id_user))
        res=cursor.fetchall()
        if res==[]:
            return render(request,'mes_reservation.html',{})
        else :
            resultats=[]
            keys = ['id', 'arrivee', 'depart']
            for i in res:
                result = dict(zip(keys, i))
                resultats.append(result)
            liste_reservation = {item['id']: { 'arrivee': item['arrivee'],'depart': item['depart']} for item in resultats}
            print(liste_reservation)
            context = {
                'reservation': liste_reservation,
            }
            cursor.close()
            conn.close()
            return render(request,'mes_reservation.html',context)
    except Exception as e:
        print(str(e))  # Afficher l'erreur pour le débogage
        message='Erreur route'
        return render(request,'mes_reservation.html',{})
    
    


def annuler(request):
    if request.method=="POST":
        id_reservation = request.POST.get('id_reservation')
   
    try:
        conn = sql.connect(**config)
        cursor = conn.cursor()
        cursor.execute(" DELETE FROM `app_reservation_reservations_vol` WHERE `app_reservation_reservations_vol`.`id` = {} ".format(int(id_reservation
        )))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('mes_reservations')
    except Exception as e:
        print(str(e))  # Afficher l'erreur pour le débogage
        message='Erreur route'
        return render(request,'mes_reservations.html',{})
    



def deconnexion(request):
    # Supprimer la session
    request.session.flush()

    # Autres traitements de votre vue

    return redirect(index)


# def profil(request):
#     # Récupérer les informations de profil de l'utilisateur (exemple)
#     utilisateur = request.user
#     nom = utilisateur.nom
#     prenom = utilisateur.prenom
#     email = utilisateur.email
#     telephone = utilisateur.telephone
#     adresse = utilisateur.adresse
#     mot_de_passe = utilisateur.mot_de_passe


#     context = {
#         'nom': nom,
#         'prenom': prenom,
#         'email': email,
#         'telephone':telephone,
#         'adresse':adresse,
#         'mot_de_passe':mot_de_passe
#     }

#     return render(request, 'profil.html', context)

# from django.shortcuts import render
# from .models import Utilisateur
# from django.contrib.auth.decorators import login_required
# from django.core.exceptions import ObjectDoesNotExist


# def profil(request):
#     # ...
#   utilisateur = Utilisateur.objects.get(id=request.user.id)
#   print(utilisateur.id)  # Vérifier l'ID dans la console


#   try:
#     utilisateur = Utilisateur.objects.get(id=request.user.id)
#   except ObjectDoesNotExist:
#     print("Utilisateur non trouvé")




# def profil(request):
#     utilisateur = Utilisateur.objects.get(id=request.user.id)
#     context = {
#         'user': utilisateur
#     }
#     return render(request, 'profil.html', context)




# def profil(request):
#     utilisateur = Utilisateur.objects.get(id=request.user.id)
#     context = {
#         'utilisateur': utilisateur
#     }
#     return render(request, 'app_reservation/profil.html', context)



#@login_required

def profil(request):
    utilisateur = request.user
    print(utilisateur)
    if hasattr(utilisateur, 'nom'):  # Vérifier si l'utilisateur a l'attribut 'nom'
        nom = utilisateur.nom
        prenom = utilisateur.prenom
        adresse = utilisateur.adresse
        email = utilisateur.email
        telephone = utilisateur.telephone
    else:
        nom = ""
        prenom = ""
        adresse = ""
        email = ""
        telephone = ""

    context = {
        'nom': nom,
        'prenom': prenom,
        'adresse': adresse,
        'email': email,
        'telephone': telephone,
    }

    return render(request, 'profil.html', context)

