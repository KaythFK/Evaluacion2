from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Compromiso, ObservacionCompromiso

class CompromisoAdmin(admin.ModelAdmin):
    # Se seleccionan los campos más representativos para la vista de tabla
    list_display = ("id_compromiso", "origen", "solicitante", "territorio", "estado", "fecha_comprometida", "id_funcionario")
    # Se incluyen campos de texto y descriptivos en la barra de búsqueda
    search_fields = ("origen", "solicitante", "territorio", "apoyo")
    # Se utilizan campos categóricos y fechas para los filtros laterales
    list_filter = ("estado", "territorio", "fecha_registro")

class ObservacionCompromisoAdmin(admin.ModelAdmin):
    # Se muestra el identificador, la fecha, el compromiso al que pertenece y el texto
    list_display = ("id_observacioncomp", "id_compromiso", "fecha", "texto")
    # Se habilita la búsqueda dentro del contenido de la observación
    search_fields = ("texto",)
    # Se permite filtrar cronológicamentelas observaciones
    list_filter = ("fecha",)

# Registro de los modelos en el sitio de administración
admin.site.register(Compromiso, CompromisoAdmin)
admin.site.register(ObservacionCompromiso, ObservacionCompromisoAdmin)