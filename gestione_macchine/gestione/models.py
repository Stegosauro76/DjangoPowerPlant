from django.db import models



class Stabilimento(models.Model):
      nome = models.CharField(max_length=100)
      descrizione = models.TextField()
def __str__(self):

   return self.nome

class Macchinario(models.Model):
    codiceMacchinario = models.CharField(max_length=100,primary_key=True)
    nome = models.CharField(max_length=100)
    descrizione = models.TextField()
    stabilimento = models.ForeignKey(Stabilimento, on_delete=models.CASCADE)
    modello = models.CharField(max_length=24)

