from django.shortcuts import render, redirect
from django.db.models import Count
from django.http import JsonResponse
from .models import Macchinario,Stabilimento,WorkHour
from .forms import MacchinarioForm, StabilimentoForm,WorkHourForm

def lista_macchine(request):
    macchine = Macchinario.objects.all()
    return render(request, 'gestione/lista_macchine.html', {'macchine': macchine})

def lista_turni(request):
    workhour = WorkHour.objects.all()
    return render(request, 'gestione/lista_turni.html', {'workhour': workhour})


def lista_stab(request):
    stab = Stabilimento.objects.all()
    return render(request, 'gestione/lista_stab.html', {'stabilimento':stab})

def home(request):
    stabilimento = Stabilimento.objects.annotate(numero_macchinari=Count('macchinario'))

    macchine = Macchinario.objects.all()
    
    workhour = WorkHour.objects.all()
    macchine_stabilimenti = Stabilimento.objects.all().prefetch_related('macchinario')# segue la chiave esterna
    macchine_stabilimenti = {
        'macchine_stabilimenti': macchine_stabilimenti ,
    }
       
    
    stabilimenti_dict = [{
        'nome': stab.nome,
        'numero_macchinari': stab.numero_macchinari,
    } for stab in stabilimento]

    content = {
        'stabilimento': stabilimento, 
        'macchine': macchine,
        'workhour': workhour,
        'stabilimenti_dict': stabilimenti_dict,
        'macchine_stabilimenti ': macchine_stabilimenti ,
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



def filtra_stab(request, nome):
    stab = None
    macchinari = []

    if nome:
        # Filtra lo stabilimento in base al nome
        stab = Stabilimento.objects.filter(nome__icontains=nome).first()
        
        if stab:
          
                 macchinari = list(stab.macchinario.values('codiceMacchinario', 'nome')) 

    # Check if the request is an AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        
        if stab:
            stab_data = {
                'nome': stab.nome,
            }
        else:
            stab_data = None
        
        return JsonResponse({'stab': stab_data, 'macchinari': macchinari}) #se la richiesta è ajax restituisce i dati in formato json
   
    return render(request, 'gestione/filtra_stab.html', {'stab': stab, 'macchinari': macchinari})