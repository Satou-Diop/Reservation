import os
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import Utilisateur
import mysql.connector as sql
from datetime import datetime
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import json
from django.shortcuts import render
from datetime import datetime

config = {
    'user': 'fatou',
    'password': 'SEYnabou16',
    'host': 'localhost',
    'database': 'bd_app',
}
# Établir une connexion à la base de données
conn = sql.connect(**config)
cursor = conn.cursor()       
nom,prenom,email,telephone,adresse,mot_de_passe='','','','','',''
# Create your views here.
def index(request):
    # Definir les variables globale
    return render(request, 'index.html',  {})
     

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
                    keys = ['id', 'nom', 'prenom', 'addresse', 'email', 'telephone']
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
    return render(request, 'reservation_voiture.html', context)

#LES VOITURES


def car_list(request):
    if request.method =="POST":
        Lieulocation  = request.POST.get('Lieulocation')
        Datelocation  = request.POST.get('Datelocation')
        Retourlocation  = request.POST.get('Retourlocation')

        try:
            message=''
            conn = sql.connect(**config)
            cursor = conn.cursor()
            requete="select * from app_reservation_voiture where localisation LIKE '%{}%'  ".format(Lieulocation)
            cursor.execute(requete)
            res=cursor.fetchall()
            print(res)
            if res==[]:
                # request.session['hotel_info'] = {
                #     'lieu':lieu,
                #     'arrivee':date_reservation,
                #     'depart':date_restitution,
                #     'nombre':nombre
                # }
                return render(request, 'car_list.html', {})
                
            else :
                resultats=[]
                keys = ['id', 'marque','modele','localisation','annee','type','prix', 'nombre_place','photo','disponible']
                for i in res:
                    result = dict(zip(keys, i))
                    resultats.append(result)
                liste_voiture= {item['id']: {'marque': item['marque'], 'modele': item['modele'],'localisation': item['localisation'],'annee': item['annee'],'type': item['type'],'prix': item['prix'],'nombre_place': item['nombre_place'],'photo': item['photo'],'disponible': item['disponible']} for item in resultats}
                context = {'liste_voiture': liste_voiture}
                cursor.close()
                conn.close()
                # Stocker le dictionnaire dans la session
                # request.session['voiture_info'] = {
                #     'lieu':Lieulocation,
                #     'arrivee':Datelocation,
                #     'depart':Retourlocation,
                # }
                
                return render(request, 'car_list.html', context)
            
        except Exception as e:
            print(str(e))  # Afficher l'erreur pour le débogage
            message='Erreur route'
            return render(request, 'connexion.html', {'erreur_message': message})


# current_dir = os.getcwd()

#     # Construire le chemin d'accès complet au fichier car_data.json

# file_path = os.path.join(current_dir, 'Data','car_data.json')

# with open(file_path) as json_file:
#     cars = json.load(json_file)
        
    # return render(request, 'car_list.html', {'cars': cars})


def deconnexion(request):
    # Supprimer la session
    request.session.flush()

    # Autres traitements de votre vue

    return redirect(index)




def reservation_voiture(request):
 
    return render(request,'reservation_voiture.html',{})

   



def paiement(request):

    return render(request,'paiement.html',{})



def voir_plus(request):
    id_voiture  = request.POST.get('id_voiture')
    print(id_voiture)
    try:
        message=''
        conn = sql.connect(**config)
        cursor = conn.cursor()
        requete="select * from app_reservation_voiture where id = {}  ".format(int(id_voiture))
        cursor.execute(requete)
        res=cursor.fetchall()
        print(res)
        if res==[]:
            # request.session['hotel_info'] = {
            #     'lieu':lieu,
            #     'arrivee':date_reservation,
            #     'depart':date_restitution,
            #     'nombre':nombre
            # }
            return render(request, 'voir_plus.html', {})
            
        else :
            resultats=[]
            keys = ['id', 'marque','modele','localisation','annee','type','prix', 'nombre_place','photo','disponible']
            for i in res:
                result = dict(zip(keys, i))
                resultats.append(result)
            liste_voiture= {item['id']: {'marque': item['marque'], 'modele': item['modele'],'localisation': item['localisation'],'annee': item['annee'],'type': item['type'],'prix': item['prix'],'nombre_place': item['nombre_place'],'photo': item['photo'],'disponible': item['disponible']} for item in resultats}
            context = {'liste_voiture': liste_voiture}
            cursor.close()
            conn.close()
            # Stocker le dictionnaire dans la session
            # request.session['voiture_info'] = {
            #     'lieu':Lieulocation,
            #     'arrivee':Datelocation,
            #     'depart':Retourlocation,
            # }
            
            return render(request, 'voir_plus.html', context)
        
    except Exception as e:
        print(str(e))  # Afficher l'erreur pour le débogage
        message='Erreur route'
        return render(request, 'connexion.html', {'erreur_message': message})

   


def resultat(request):

    return render(request,'resultat.html',{})


def my_reservations(request):
    
    if 'info_utilisateur' in request.session:
        info_utilisateur = request.session['info_utilisateur']
        if 'id' in info_utilisateur:
            id_user = info_utilisateur['id']
    try:
        conn = sql.connect(**config)
        cursor = conn.cursor()
        requete="INSERT INTO app_reservation_reservations_hotel (id, date_reservation, date_restitution, chambre_id, utilisateur_id) VALUES (NULL, '{}', '{}', '{}', '{}');".format(arrivee_datetime,depart_datetime,int(id_chambre),int(id_user))
        cursor.execute(requete)
        # Valider les modifications
        conn.commit()
        cursor.execute("SELECT * FROM `app_reservation_reservations_hotel` where utilisateur_id ='{}' ".format(id_user))
        res=cursor.fetchall()
        if res==[]:
            return render(request,'my_reservations.html',{})
        else :
            keys = ['id', 'arrivee', 'depart']
            reservations = dict(zip(keys, res[0]))
            context = {
                'reservation': reservations,
            }
            cursor.close()
            conn.close()
            return render(request,'my_reservations.html',context)
    except Exception as e:
        print(str(e))  # Afficher l'erreur pour le débogage
        message='Erreur route'
        return render(request,'my_reservations.html',{})
   



