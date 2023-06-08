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
    path("reservation_voiture/", views.reservation_voiture, name='reservation_voiture'),
    path("connexion/", views.connexion, name='connexion'),
    path("inscription/", views.inscription, name='inscription'),
    path("car_list/", views.car_list, name='car_list'),
    path("paiement/", views.paiement, name='paiement'),
    path("voir_plus/", views.voir_plus, name='voir_plus')


    # path('res/', views.res_app, name='res_app')

]