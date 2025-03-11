from django.urls import path
from .views import lista_macchine, aggiungi_macchina,modifica_macchina,home, lista_stab,aggiungi_stabilimento,aggiungi_ore_lavorate,lista_turni

urlpatterns = [
    path('macchine/', lista_macchine, name='lista_macchine'),
    path('macchine/aggiungi/', aggiungi_macchina, name='aggiungi_macchina'),
    path('stab/aggiungi/', aggiungi_stabilimento, name='aggiungi_stab'),
      path('macchine/modifica/<int:pk>/', modifica_macchina, name='modifica_macchina'),
      path('',home, name='home'),
      path('stab/', lista_stab, name='lista_stab'),
      path('record/',aggiungi_ore_lavorate,  name='record_work_hours'),
      path('turni/',lista_turni,name="lista_turni"),
]