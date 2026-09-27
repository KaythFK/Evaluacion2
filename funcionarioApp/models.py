from django.db import models

# Create your models here.
class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=60)
    apellido_materno = models.CharField(max_length=60, blank=True, null=True)
    estado = models.IntegerField()
    telefono = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(unique=True, max_length=150)
    id_cargo = models.ForeignKey('Cargo', models.DO_NOTHING, db_column='id_cargo')
    id_delegacion = models.ForeignKey('delegacionesApp.Delegacion', models.DO_NOTHING, db_column='id_delegacion')
    id_rol = models.ForeignKey('CatalogoRoles', models.DO_NOTHING, db_column='id_rol')

    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno}"
    class Meta:
        managed = False
        db_table = 'funcionario'

#Tablas alojadas temporalmente


class Cargo(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    vigencia = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        managed = False
        db_table = 'cargo'


class CargoServicio(models.Model):
    pk = models.CompositePrimaryKey('id_servicios', 'id_cargo')
    id_servicios = models.ForeignKey('CatalagoServicio', models.DO_NOTHING, db_column='id_servicios')
    id_cargo = models.ForeignKey('Cargo', models.DO_NOTHING, db_column='id_cargo')

    class Meta:
        managed = False
        db_table = 'cargo_servicio'





class CatalagoServicio(models.Model):
    id_servicios = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=45)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        managed = False
        db_table = 'catalago_servicio'


class CatalogoRoles(models.Model):
    id_roles = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        managed = False
        db_table = 'catalogo_roles'

class Auditoria(models.Model):
    id_auditoria = models.IntegerField(primary_key=True)
    evento = models.CharField(max_length=150)
    fecha = models.DateTimeField()
    entidad = models.CharField(max_length=100)
    identificador = models.IntegerField()
    valor_anterior = models.JSONField(blank=True, null=True)
    valor_nuevo = models.JSONField(blank=True, null=True)
    funcionario_id_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='Funcionario_id_funcionario')  # Field name made lowercase.

    def __str__(self):
        return f"Auditoría {self.id_auditoria} - {self.evento}"
    
    class Meta:
        managed = False
        db_table = 'auditoria'

