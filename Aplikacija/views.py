from django.shortcuts import render
from .models import Linija, VozniRed

def home(request):
    linije = Linija.objects.all()
    return render(request, 'home.html', {'linije': linije})

from .models import VozniRed

def vozniRed(request):
    redovi = VozniRed.objects.all()
    return render(request, 'vozniRed.html', {'redovi': redovi})

def kontakt(request):
    return render(request, 'kontakt.html')

def oNama(request):
    return render(request, 'oNama.html')

def kupiKartu(request):
    return render(request, 'kupiKartu.html')

def liTaxi(request):
    return render(request, 'liTaxi.html')

def destinacije(request):
    return render(request, 'destinacije.html')