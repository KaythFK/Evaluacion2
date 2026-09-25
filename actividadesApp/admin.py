from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Actividad, Meta, Periodo, Indicador, CatalagoItem, Evidencia, Validacion

class ActividadAdmin(admin.ModelAdmin):
    list_display = ("id_actividad", "fecha", "estado", "contacto", "id_funcionario")
    search_fields = ("solicitud_problema", "accion", "contacto", "telefono")
    list_filter = ("estado", "fecha")

class MetaAdmin(admin.ModelAdmin):
    list_display = ("id_meta", "valor_objetivo", "unidad", "id_periodo", "id_funcionario")
    search_fields = ("unidad",)
    list_filter = ("id_periodo", "id_cargo")

class PeriodoAdmin(admin.ModelAdmin):
    list_display = ("id_periodo", "nombre", "fecha_inicio", "fecha_termino", "estado")
    search_fields = ("nombre",)
    list_filter = ("estado", "fecha_inicio")

class IndicadorAdmin(admin.ModelAdmin):
    list_display = ("id_indicador", "avance", "cumplimiento", "semaforo", "fecha_calculo")
    search_fields = ("semaforo",)
    list_filter = ("semaforo", "fecha_calculo")

class CatalagoItemAdmin(admin.ModelAdmin):
    list_display = ("id_item", "nombre")
    search_fields = ("nombre",)

class EvidenciaAdmin(admin.ModelAdmin):
    list_display = ("id_evidencia", "fecha", "estado_revision", "id_actividad", "id_funcionario_carga")
    search_fields = ("archivo_vinculo", "estado_revision")
    list_filter = ("estado_revision", "fecha")

class ValidacionAdmin(admin.ModelAdmin):
    list_display = ("id_validacion", "decision", "fecha", "resultado", "id_validador")
    search_fields = ("observacion", "resultado", "decision")
    list_filter = ("decision", "fecha")

# Registramos cada modelo con su configuración
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Meta, MetaAdmin)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(Indicador, IndicadorAdmin)
admin.site.register(CatalagoItem, CatalagoItemAdmin)
admin.site.register(Evidencia, EvidenciaAdmin)
admin.site.register(Validacion, ValidacionAdmin)