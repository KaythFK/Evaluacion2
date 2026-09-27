from django.contrib import admin
from django.urls import path, include
from funcionarioApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio, name='inicio'),
    path('delegaciones/', include('delegacionesApp.urls')),
    path('funcionario/', include('funcionarioApp.urls')),
    path('', views.main, name='main'),
    path('tubo/', include('agendaApp.urls')),
    path('actividades/', include('actividadesApp.urls'))
]
