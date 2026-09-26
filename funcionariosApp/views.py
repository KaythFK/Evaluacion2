from django.shortcuts import render
from .models import Funcionario

def main(request):
    return render(request, 'tubo/main.html')

def inicio(request):
    return render(request, 'funcionarios/inicio.html')

def directorio_funcionarios(request):
    lista_funcionarios = Funcionario.objects.all()
    return render(request, 'funcionarios/directorio.html', {'funcionarios': lista_funcionarios})