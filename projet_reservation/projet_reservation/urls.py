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

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name='index'),
    path("chambre/", views.chambre, name='chambre'),
    path("reservation/", views.reservation, name='reservation'),
    path("mes_reservations/", views.mes_reservations, name='mes_reservations'),
    path("paiement/", views.paiement, name='paiement'),
    path("connexion/", views.connexion, name='connexion'),
    path("deconnexion/", views.deconnexion, name='deconnexion'),
    path("inscription/", views.inscription, name='inscription'),
    path("annuler/", views.annuler, name='annuler'),
    path("profil/", views.profil, name='profil')
    
]