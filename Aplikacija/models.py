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