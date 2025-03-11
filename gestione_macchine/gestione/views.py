from django.shortcuts import render, redirect,get_object_or_404
from .models import Macchinario,Stabilimento
from .forms import MacchinarioForm, StabilimentoForm

def lista_macchine(request):
    macchine = Macchinario.objects.all()
    return render(request, 'gestione/lista_macchine.html', {'macchine': macchine})

def lista_stab(request):
    stab = Stabilimento.objects.all()
    return render(request, 'gestione/lista_stab.html', {'stabilimento':stab})

def home(request):
    stab = Stabilimento.objects.all()
    macchine = Macchinario.objects.all()
    content={
        'stabilimento':stab,
        'macchine':macchine
    }
    return render(request, 'gestione/home.html',{'content':content})

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

def delete_macchinario(request, codiceMacchinario):

    macchinario = get_object_or_404(Macchinario, codiceMacchinario=codiceMacchinario)


    if request.method == 'POST':

        macchinario.delete()

        return redirect('lista_macchine')  


    return render(request, 'delete_macchinario.html', {'macchinario': macchinario})