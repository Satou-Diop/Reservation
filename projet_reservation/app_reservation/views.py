from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import Utilisateur
import mysql.connector


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

def connexion(request):
    if request.method=="POST":
        message=''
        email = request.POST.get('email')
        mot_de_passe = request.POST.get('mot_de_passe')
        if(email!='' and mot_de_passe!=''): 
            try:
                message=''
                utilisateur = Utilisateur.objects.filter(email__iexact=email, mot_de_passe__exact=mot_de_passe).first()
                print(utilisateur)
                if utilisateur :
                    return redirect('/')  # Rediriger vers la page d'accueil après l'inscription réussie   
                else :
                    message='Login ou mot de passe incorrect'
                    return render(request, 'connexion.html', {'erreur_message': message})
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
            return HttpResponse('Les motes de passe ne corresponde pas')
        try:
            utilisateur = Utilisateur.objects.create(nom=nom, prenom=prenom, email=email, telephone=telephone,adresse=adresse,mot_de_passe=mot_de_passe)
            utilisateur.save()
            return redirect('login')  # Rediriger vers la page d'accueil après l'inscription réussie
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

