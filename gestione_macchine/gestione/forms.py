# gestione_macchinari/forms.py
from django import forms
from .models import Stabilimento, Macchinario,WorkHour

from django.db.models import Sum
from django.contrib.auth.models import User

class StabilimentoForm(forms.ModelForm):
    class Meta:
        model = Stabilimento
        fields = ['nome', 'descrizione']  

class MacchinarioForm(forms.ModelForm):
    class Meta:
        model = Macchinario
        fields = '__all__'
        

class WorkHourForm(forms.ModelForm):
    class Meta:
        model = WorkHour  
        fields = '__all__'
    