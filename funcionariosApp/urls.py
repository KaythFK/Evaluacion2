from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('inicio/', views.inicio, name='inicio'),
    path('directorio/', views.directorio_funcionarios, name='directorio_funcionarios'),
]