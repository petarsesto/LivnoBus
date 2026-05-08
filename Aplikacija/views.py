from django.shortcuts import render
from .models import Linija, VozniRed

def home(request):
    linije = Linija.objects.all()
    return render(request, 'home.html', {'linije': linije})

from .models import VozniRed

def vozni_red(request):
    redovi = VozniRed.objects.all()
    return render(request, 'vozniRed.html', {'redovi': redovi})