from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Funcionario, Cargo, CargoServicio, CatalagoServicio, CatalogoRoles, Auditoria

class FuncionarioAdmin(admin.ModelAdmin):
    # Mostramos los datos personales básicos y sus asignaciones operativas
    list_display = ("id_funcionario", "nombres", "apellido_paterno", "apellido_materno", "estado", "id_cargo", "id_delegacion")
    # Permitimos buscar al personal por nombre, apellidos, correo o teléfono
    search_fields = ("nombres", "apellido_paterno", "apellido_materno", "correo", "telefono")
    # Agrupamos por estado activo/inactivo, rol en el sistema o ubicación
    list_filter = ("estado", "id_cargo", "id_delegacion", "id_rol")

class CargoAdmin(admin.ModelAdmin):
    list_display = ("id_cargo", "nombre", "vigencia")
    search_fields = ("nombre",)
    list_filter = ("vigencia",)

class CatalagoServicioAdmin(admin.ModelAdmin):
    list_display = ("id_servicios", "nombre")
    search_fields = ("nombre",)

class CatalogoRolesAdmin(admin.ModelAdmin):
    list_display = ("id_roles", "nombre")
    search_fields = ("nombre",)

class AuditoriaAdmin(admin.ModelAdmin):
    # Muestra un resumen rápido de quién hizo qué y cuándo
    list_display = ("id_auditoria", "evento", "entidad", "fecha", "funcionario_id_funcionario")
    # Útil para rastrear eventos específicos o tablas afectadas
    search_fields = ("evento", "entidad")
    list_filter = ("entidad", "fecha")

#class CargoServicioAdmin(admin.ModelAdmin):
    # Tabla intermedia o puente
    #list_display = ("id_servicios", "id_cargo")

# Registramos todas las clases en el sitio
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(CatalagoServicio, CatalagoServicioAdmin)
admin.site.register(CatalogoRoles, CatalogoRolesAdmin)
admin.site.register(Auditoria, AuditoriaAdmin)
#admin.site.register(CargoServicio, CargoServicioAdmin)