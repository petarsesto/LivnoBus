from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vozni-red/', views.vozniRed, name='VozniRed'),
    path('kontakt/', views.kontakt),
    path('o-nama/', views.oNama),
    path('kupi-kartu/', views.kupiKartu),
    path('li-taxi/', views.liTaxi),
    path('destinacije/', views.destinacije, name="destinacije"),
    path("destinacije/<slug:slug>/",views.destinacija_detalji,name="destinacija_detalji"),
    path('mostar/', views.mostar, name='mostar'),
    path('split/', views.split, name='split'),
    path('sarajevo/', views.sarajevo, name="sarajevo"),
    path('jajce/', views.jajce, name='jajce'),
    path('zagreb/', views.zagreb, name='zagreb'),
    path('tuzla/', views.tuzla, name="tuzla"),
    path('banjaluka/', views.banjaluka, name='banjaluka'),
    path('zenica/', views.zenica, name='zenica'),
    path('munchen/', views.munchen, name="munchen"),
    path('augsburg/', views.augsburg, name="augsburg"),
    path('uspjesna-rezervacija/', views.uspjesnaRezervacija, name="uspjesnaRezervacija"),
]