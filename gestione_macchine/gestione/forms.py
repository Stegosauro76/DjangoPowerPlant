# gestione_macchinari/forms.py
from django import forms
from .models import Stabilimento, Macchinario,WorkHour



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
    