from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'funcionarios/inicio.html')

def main(request):
    return render(request, 'main.html')