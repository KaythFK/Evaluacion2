from django.db import models
from delegacionesApp.models import Delegacion  

class Cargo(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    vigencia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargo'

    def __str__(self):
        return str(self.nombre)

class CatalogoRoles(models.Model):
    id_roles = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'catalogo_roles'

    def __str__(self):
        return str(self.nombre)

class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=60)
    apellido_materno = models.CharField(max_length=60, blank=True, null=True)
    estado = models.IntegerField()
    telefono = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(unique=True, max_length=150)
    
    id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_cargo')
    id_delegacion = models.ForeignKey(Delegacion, models.DO_NOTHING, db_column='id_delegacion')
    id_rol = models.ForeignKey(CatalogoRoles, models.DO_NOTHING, db_column='id_rol')

    class Meta:
        managed = False
        db_table = 'funcionario'

    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno}"