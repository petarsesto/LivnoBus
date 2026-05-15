from django.shortcuts import render
from .models import Linija, VozniRed

def home(request):
    linije = Linija.objects.all()
    return render(request, 'home.html', {'linije': linije})

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

def mostar(request):
    return render(request, 'mostar.html')

def split(request):
    return render(request, 'split.html')

def sarajevo(request):
    return render(request, 'sarajevo.html')

def jajce(request):
    return render(request, 'jajce.html')

def zagreb(request):
    return render(request, 'zagreb.html')

def tuzla(request):
    return render(request, 'tuzla.html')

def banjaluka(request):
    return render(request, 'banjaluka.html')

def zenica(request):
    return render(request, 'zenica.html')

def munchen(request):
    return render(request, 'munchen.html')

def augsburg(request):
    return render(request, 'augsburg.html')