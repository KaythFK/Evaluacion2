from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Delegacion

class DelegacionAdmin(admin.ModelAdmin):
    # Se muestran los datos esenciales para identificar rápidamente la oficina y su encargado
    list_display = ("id_delegacion", "nombre", "territorio", "estado", "responsable")
    # Se omite 'numero_calle' de la búsqueda porque los números generan errores en searcields
    search_fields = ("nombre", "territorio", "calle")
    # Filtros ideales para agrupar las delegaciones por su zona geográfica o estado operativo
    list_filter = ("estado", "territorio")

admin.site.register(Delegacion, DelegacionAdmin)