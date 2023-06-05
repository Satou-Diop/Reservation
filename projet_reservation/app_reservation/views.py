from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import Utilisateur
import mysql.connector as sql
from datetime import datetime

config = {
    'user': 'admin_reservation',
    'password': 'Reservation123@',
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
        mot_de_passe2 =request.POST.get('mot_de_passe2')
        if mot_de_passe!=mot_de_passe2:
            return HttpResponse('Les mots de passe ne correspondent pas')
        try:
            conn = sql.connect(**config)
            cursor = conn.cursor()
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
    if 'hotel_info' in request.session:

        if request.POST.get('lieu')!= request.session['hotel_info']['lieu'] and request.POST.get('lieu') :
            lieu = request.POST.get('lieu')
        else: 
            lieu = request.session['hotel_info']['lieu']

        if request.POST.get('date_reservation') != request.session['hotel_info']['arrivee'] and request.POST.get('date_reservation') :
            date_reservation  = request.POST.get('date_reservation')
        else: 
            date_reservation = request.session['hotel_info']['arrivee']

        if request.POST.get('date_restitution') != request.session['hotel_info']['depart'] and request.POST.get('date_restitution') :
            date_restitution  = request.POST.get('date_restitution')
        else: 
            date_restitution = request.session['hotel_info']['depart']

        if request.POST.get('nombre') != request.session['hotel_info']['nombre'] and request.POST.get('nombre') :
            nombre  = request.POST.get('nombre')
        else: 
            nombre = request.session['hotel_info']['nombre']
              
        
    else:
       
        lieu  = request.POST.get('lieu')
        date_reservation  = request.POST.get('date_reservation')
        date_restitution  = request.POST.get('date_restitution')
        nombre  = request.POST.get('nombre')
    
    try:
        message=''
        conn = sql.connect(**config)
        cursor = conn.cursor()
        requete="select * from app_reservation_hotel where nom LIKE '%{}%' or ville LIKE '%{}%' ".format(lieu,lieu)
        cursor.execute(requete)
        res=cursor.fetchall()
        if res==[]:
            request.session['hotel_info'] = {
                'lieu':lieu,
                'arrivee':date_reservation,
                'depart':date_restitution,
                'nombre':nombre
            }
            return render(request, 'resultat.html', {})
            
        else :
            resultats=[]
            keys = ['id', 'nom', 'code','ville','photo']
            for i in res:
                result = dict(zip(keys, i))
                resultats.append(result)
            liste_hotels = {item['id']: {'nom': item['nom'], 'code': item['code'],'ville': item['ville'],'photo': item['photo']} for item in resultats}
            context = {'liste_hotels': liste_hotels}
            cursor.close()
            conn.close()
            # Stocker le dictionnaire dans la session
            request.session['hotel_info'] = {
                'lieu':lieu,
                'arrivee':date_reservation,
                'depart':date_restitution,
                'nombre':nombre
            }
            
            return render(request, 'resultat.html', context)
        
    except Exception as e:
        print(str(e))  # Afficher l'erreur pour le débogage
        message='Erreur route'
        return render(request, 'connexion.html', {'erreur_message': message})


def chambre(request):
    
    id_hotel  = request.POST.get('id_hotel')
    request.session['id_hotel']=request.POST.get('id_hotel')
    try:
        conn = sql.connect(**config)
        cursor = conn.cursor()
        requete1="select * from app_reservation_hotel where id_hotel='{}' ".format(id_hotel)
        cursor.execute(requete1)
        res=cursor.fetchall()
        keys = ['id', 'nom', 'code','ville','photo']
        hotel = dict(zip(keys, res[0]))
        print(hotel)
        context = {
                'hotel': hotel,
                }
        requete2="select * from app_reservation_chambre where hotel_id='{}' ".format(id_hotel)
        cursor.execute(requete2)
        res=cursor.fetchall()
        if res==[]:
            return render(request, 'chambre.html', context)
            
        else :
            resultats=[]
            keys = ['id', 'type', 'description','prix','nombre','photo']
            for i in res:
                result = dict(zip(keys, i))
                resultats.append(result)
            liste_chambre = {item['id']: { 'type': item['type'],'description': item['description'],'prix': item['prix'],'nombre': item['nombre'],'photo': item['photo']} for item in resultats}
            
            context = {
                'hotel': hotel,
                'liste_chambre': liste_chambre}
            cursor.close()
            conn.close()
            # Stocker le dic{{hotel.nom}}tionnaire dans la session
            return render(request, 'chambre.html', context)
        
    except Exception as e:
        print(str(e))  # Afficher l'erreur pour le débogage
        message='Erreur route'
        return render(request, 'chambre.html', {'erreur_message': message})


def deconnexion(request):
    # Supprimer la session
    request.session.flush()

    # Autres traitements de votre vue

    return redirect(index)

def reservation(request):
    id_chambre  = request.POST.get('id_chambre')
    if 'info_utilisateur' in request.session:
        info_utilisateur = request.session['info_utilisateur']
        if 'id' in info_utilisateur:
            id_user = info_utilisateur['id']
    if 'hotel_info' in request.session:
        arrivee = request.session['hotel_info']['arrivee']
        arrivee_datetime = datetime.strptime(arrivee, '%Y-%m-%d').replace(hour=0, minute=0, second=0)
        depart = request.session['hotel_info']['depart']
        depart_datetime = datetime.strptime(depart, '%Y-%m-%d').replace(hour=0, minute=0, second=0)

    print(arrivee_datetime,depart_datetime,int(id_chambre),int(id_user))
    try:
        message=''
        conn = sql.connect(**config)
        cursor = conn.cursor()
        requete="INSERT INTO app_reservation_reservations_hotel (id, date_reservation, date_restitution, chambre_id, utilisateur_id) VALUES (NULL, '{}', '{}', '{}', '{}');".format(arrivee_datetime,depart_datetime,int(id_chambre),int(id_user))
        cursor.execute(requete)
        # Valider les modifications
        conn.commit()
        cursor.execute("SELECT * FROM `app_reservation_reservations_hotel` ORDER BY id DESC LIMIT 1;")
        res=cursor.fetchall()
        keys = ['id', 'arrivee', 'depart', 'id_chambre']
        reservations = dict(zip(keys, res[0]))
        cursor.execute(" SELECT * FROM app_reservation_chambre WHERE id = '{}' ".format(reservations['id_chambre']))
        res=cursor.fetchall()
        keys = ['id', 'type', 'desc','prix', 'nombre']
        chambre = dict(zip(keys, res[0]))
        context = {
                'reservation': reservations,
                'chambre':chambre
                }
        cursor.close()
        conn.close()
        return render(request, 'reservation.html', context)
    except Exception as e:
        print(str(e))  # Afficher l'erreur pour le débogage
        message='Erreur route'
        return render(request, 'connexion.html', {'erreur_message': message})


    


def paiement(request):
    id_reservation  = request.POST.get('id_reservation')

    return render(request,'paiement.html',{'id_reservation' :id_reservation})