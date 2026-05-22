from django.db import models


class Linija(models.Model):
    naziv = models.CharField(max_length=100)
    polaziste = models.CharField(max_length=100)
    odrediste = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.polaziste} → {self.odrediste}"


class VozniRed(models.Model):
    linija = models.ForeignKey(Linija, on_delete=models.CASCADE)
    vrijeme_polaska = models.TimeField()
    vrijeme_dolaska = models.TimeField()

    def __str__(self):
        return f"{self.linija} ({self.vrijeme_polaska})"


class Karta(models.Model):
    linija = models.ForeignKey(Linija, on_delete=models.CASCADE)
    ime_putnika = models.CharField(max_length=100)
    broj_telefona = models.CharField(max_length=20)
    datum_putovanja = models.DateField()
    broj_karata = models.IntegerField()

    def __str__(self):
        return f"{self.ime_putnika} - {self.linija}"


# 🚕 LI TAXI (posebna usluga)
class TaxiRezervacija(models.Model):
    ime = models.CharField(max_length=100)
    broj_telefona = models.CharField(max_length=20)
    lokacija_polaska = models.CharField(max_length=200)
    lokacija_odredista = models.CharField(max_length=200)
    vrijeme = models.DateTimeField()

    def __str__(self):
        return f"{self.ime} - Taxi"


class Destinacija(models.Model):
    naziv = models.CharField(max_length=100)
    opis = models.TextField()
    slika = models.URLField()
    slug = models.SlugField(unique=True)
    trajanje = models.CharField(max_length=50)
    cijena = models.CharField(max_length=50)
    polasci = models.CharField(max_length=50)
    wifi = models.CharField(max_length=50)
    detalji = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.naziv