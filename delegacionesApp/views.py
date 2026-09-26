from django.shortcuts import render
from .models import Delegacion

def delegaciones(request):
    lista_delegaciones = Delegacion.objects.all()
    context = {
        'delegaciones': lista_delegaciones
    }
    return render(request, 'delegaciones/inicio.html', context)