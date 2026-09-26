from django.contrib import admin
from django.urls import path, include
from funcionariosApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio, name='inicio'),
    path('delegaciones/', include('delegacionesApp.urls')),
    path('funcionarios/', include('funcionariosApp.urls')),
    path('', views.main, name='main')
]
