from django.urls import path
from .views import *

urlpatterns = [
    path('macchine/', lista_macchine, name='lista_macchine'),
    path('macchine/aggiungi/', aggiungi_macchina, name='aggiungi_macchina'),
    path('stab/aggiungi/', aggiungi_stabilimento, name='aggiungi_stab'),
      path('macchine/modifica/<int:pk>/', modifica_macchina, name='modifica_macchina'),
      path('',home, name='home'),
      path('stab/', lista_stab, name='lista_stab'),
      path('record/',aggiungi_ore_lavorate,  name='record_work_hours'),
      path('turni/',lista_turni,name="lista_turni"),
       path('stabilimento/<str:nome>/',filtra_stab, name='filtra_stab'),
      
]