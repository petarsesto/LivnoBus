from django.shortcuts import render, get_object_or_404
from .models import Linija, VozniRed, Destinacija


# HOME
def home(request):
    linije = Linija.objects.all()
    return render(request, 'home.html', {'linije': linije})


# VOZNI RED
def vozniRed(request):
    redovi = VozniRed.objects.all()
    return render(request, 'vozniRed.html', {'redovi': redovi})


# KONTAKT
def kontakt(request):
    return render(request, 'kontakt.html')


# O NAMA
def oNama(request):
    return render(request, 'oNama.html')


# KUPI KARTU
def kupiKartu(request):
    return render(request, 'kupiKartu.html')


# LI TAXI
def liTaxi(request):
    return render(request, 'liTaxi.html')


# DESTINACIJE
def destinacije(request):
    destinacije = Destinacija.objects.all()
    return render(request, 'destinacije.html', {'destinacije': destinacije})


# DESTINACIJA DETALJI
def destinacija_detalji(request, slug):
    try:
        return render(request, f"{slug}.html")
    except:
        destinacija = get_object_or_404(Destinacija, slug=slug)
        return render(request, "destinacijaDetalji.html", {
            "destinacija": destinacija
        })


# GRADOVI
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


# USPJEŠNA REZERVACIJA
def uspjesnaRezervacija(request):
    return render(request, "uspjesnaRezervacija.html")