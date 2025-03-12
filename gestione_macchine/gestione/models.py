from django.db import models



class Stabilimento(models.Model):
      #codiceStabilimento = models.CharField(max_length=242,primary_key=True,default="0")
      nome = models.CharField(max_length=100)
      descrizione = models.TextField()
      def __str__(self): #lo inserisco per poter visualizzare il nome dell'azienda come chiave esterna invece che object(13) come formato

         return f"{self.nome}"

class Macchinario(models.Model):
    codiceMacchinario = models.CharField(max_length=100,primary_key=True)
    nome = models.CharField(max_length=100)
    descrizione = models.TextField()
    stabilimento = models.ForeignKey(Stabilimento,related_name='macchinario',on_delete=models.CASCADE)
    modello = models.CharField(max_length=24)

class WorkHour(models.Model):

    employee_name = models.CharField(max_length=100)

    date = models.DateField()

    hours_worked = models.DecimalField(max_digits=5, decimal_places=1)


    def __str__(self):

        return f"{self.employee_name}"