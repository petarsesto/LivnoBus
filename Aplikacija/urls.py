from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vozni-red/', views.vozniRed, name='VozniRed'),
    path('kontakt/', views.kontakt),
    path('o-nama/', views.oNama),
    path('kupi-kartu/', views.kupiKartu),
    path('li-taxi/', views.liTaxi),
    path('destinacije/', views.destinacije),
]