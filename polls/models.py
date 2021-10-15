from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=40)
    data = models.DateTimeField('data categoria')
    def __str__(self):
        return self.categoria

class Domanda(models.Model):
    testo_domanda = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data = models.DateTimeField('data pubblicazione')
    def __str__(self):
        return self.testo_domanda

class Risposta(models.Model):
    domanda = models.ForeignKey(Domanda, on_delete=models.CASCADE)
    testo_risposta = models.CharField(max_length=200)
    voto = models.IntegerField(default=0)

