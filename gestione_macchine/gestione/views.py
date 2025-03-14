from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Macchinario,Stabilimento,WorkHour
from .forms import MacchinarioForm, StabilimentoForm,WorkHourForm

def lista_macchine(request):
    macchine = Macchinario.objects.all()
    return render(request, 'gestione/lista_macchine.html', {'macchine': macchine})

def lista_turni(request):
    workhour = WorkHour.objects.all().values('employee_name','date','hours_worked','macchinario_turno')
    return render(request, 'gestione/lista_turni.html', {'workhour': workhour})


def lista_stab(request):
    stab = Stabilimento.objects.all()
    return render(request, 'gestione/lista_stab.html', {'stabilimento':stab})

def home(request):

   

    stabilimenti = Stabilimento.objects.annotate(numero_macchinari=Count('macchinario'))

    macchine = Macchinario.objects.all()

    workhour = WorkHour.objects.all()

           

    # Create a dictionary of stabilimenti

    stabilimenti_dict = [{

        'nome': stab.nome,

        'numero_macchinari': stab.numero_macchinari,

    } for stab in stabilimenti]


    content = {

        'stabilimento': stabilimenti,  # This should be a QuerySet, not a single instance

        'macchine': macchine,

        'workhour': workhour,

        'stabilimenti_dict': stabilimenti_dict

    }

    

    return render(request, 'gestione/home.html', {'content': content})

def aggiungi_macchina(request):
    if request.method == 'POST':
        form = MacchinarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_macchine')
    else:
        form = MacchinarioForm()
    return render(request, 'gestione/aggiungi_macchina.html', {'form': form})

def modifica_macchina(request, pk):
    macchina = Macchinario.objects.get(pk=pk)
    if request.method == 'POST':
        form = MacchinarioForm(request.POST, instance=macchina)
        if form.is_valid():
            form.save()
            return redirect('lista_macchine')
    else:
        form = MacchinarioForm(instance=macchina)
    return render(request, 'gestione/modifica_macchina.html', {'form': form})

def aggiungi_stabilimento(request):
    if request.method == 'POST':
        form = StabilimentoForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('lista_stab')
    else:
        form = StabilimentoForm()
        
    return render(request, 'gestione/aggiungi_stab.html', {'form': form})


def aggiungi_ore_lavorate(request):

    if request.method == 'POST':

        form = WorkHourForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('lista_turni') 

        else:

            print(form.errors) 

    else:

        form = WorkHourForm()

    return render(request, 'gestione/work_hours.html', {'form': form})

