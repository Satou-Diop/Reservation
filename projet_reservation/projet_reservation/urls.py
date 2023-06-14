"""
URL configuration for projet_reservation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_reservation import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name='index'),
    path("resultat/", views.resultat, name='resultat'),
    path("resultatvol/", views.resultatvol, name='resultatvol'),
    path("connexion/", views.connexion, name='connexion'),
    path("inscription/", views.inscription, name='inscription'),
    path('reservation_vol/', views.reservation_vol, name='reservation_vol'),
    path('confirmation_vol/', views.confirmation_vol, name='confirmation_vol'),
    path("mes_reservations/", views.mes_reservations, name='mes_reservations'),
    path("deconnexion/", views.deconnexion, name='deconnexion'),
    path("annuler/", views.annuler, name='annuler'),
    path('profil/', views.profil, name='profil'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("paiement/", views.paiement, name='paiement'),




   
    

    
]
