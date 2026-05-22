from django.urls import path
from . import views


urlpatterns = [

    # HOME
    path('', views.home, name='home'),

    # VOZNI RED
    path('vozni-red/', views.vozniRed, name='vozni_red'),

    # KONTAKT
    path('kontakt/', views.kontakt, name='kontakt'),

    # O NAMA
    path('o-nama/', views.oNama, name='o_nama'),

    # KUPI KARTU
    path('kupi-kartu/', views.kupiKartu, name='kupi_kartu'),

    # LI TAXI
    path('li-taxi/', views.liTaxi, name='li_taxi'),

    # DESTINACIJE
    path('destinacije/', views.destinacije, name='destinacije'),

    # DESTINACIJA DETALJI
    path('destinacije/<slug:slug>/', views.destinacija_detalji, name='destinacija_detalji'),

    # GRADOVI
    path('mostar/', views.mostar, name='mostar'),
    path('split/', views.split, name='split'),
    path('sarajevo/', views.sarajevo, name='sarajevo'),
    path('jajce/', views.jajce, name='jajce'),
    path('zagreb/', views.zagreb, name='zagreb'),
    path('tuzla/', views.tuzla, name='tuzla'),
    path('banjaluka/', views.banjaluka, name='banjaluka'),
    path('zenica/', views.zenica, name='zenica'),
    path('munchen/', views.munchen, name='munchen'),
    path('augsburg/', views.augsburg, name='augsburg'),

    # USPJEŠNA REZERVACIJA
    path('uspjesna-rezervacija/', views.uspjesnaRezervacija, name='uspjesna_rezervacija'),
]