from django.shortcuts import render
from .models import Funcionario

def main(request):
    return render(request, 'main.html')

def inicio(request):
    return render(request, 'funcionario/inicio.html')

def directorio_funcionario(request):
    lista_funcionario = Funcionario.objects.all()
    return render(request, 'funcionario/directorio.html', {'funcionarios': lista_funcionario})