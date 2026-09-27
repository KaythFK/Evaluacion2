from django.db import models

# Create your models here.


class Actividad(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    solicitud_problema = models.TextField()
    accion = models.TextField()
    contacto = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=11)
    id_funcionario = models.ForeignKey('funcionarioApp.Funcionario', models.DO_NOTHING, db_column='id_funcionario')
    id_meta = models.ForeignKey('Meta', models.DO_NOTHING, db_column='id_meta')

    def __str__(self):
        return f"Actividad {self.id_actividad} - {self.estado}"

    class Meta:
        managed = False
        db_table = 'actividad'

#Clases alojadas temporalmente 

class Meta(models.Model):
    id_meta = models.AutoField(primary_key=True)
    valor_objetivo = models.DecimalField(max_digits=10, decimal_places=2)
    unidad = models.CharField(max_length=50)
    ponderador = models.DecimalField(max_digits=5, decimal_places=2)
    id_item = models.ForeignKey('CatalagoItem', models.DO_NOTHING, db_column='id_item')
    id_periodo = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='id_periodo')
    id_cargo = models.ForeignKey('funcionarioApp.Cargo', models.DO_NOTHING, db_column='id_cargo')
    id_funcionario = models.ForeignKey('funcionarioApp.Funcionario', models.DO_NOTHING, db_column='id_funcionario')

    def __str__(self):
        return f"Meta {self.id_meta} ({self.valor_objetivo} {self.unidad})"

    class Meta:
        managed = False
        db_table = 'meta'

class Periodo(models.Model):
    id_periodo = models.IntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    dias_computables = models.IntegerField()
    estado = models.IntegerField(blank=True, null=True)
    umbral_regular = models.DecimalField(max_digits=5, decimal_places=2)
    umbral_exelencia = models.DecimalField(max_digits=5, decimal_places=2)
    version_parametros = models.IntegerField()

    def __str__(self):
        return str(self.nombre)

    class Meta:
        managed = False
        db_table = 'periodo'

class Indicador(models.Model):
    id_indicador = models.AutoField(primary_key=True)
    avance = models.DecimalField(max_digits=10, decimal_places=2)
    cumplimiento = models.DecimalField(max_digits=5, decimal_places=2)
    ponderacion = models.DecimalField(max_digits=5, decimal_places=2)
    ajuste = models.DecimalField(max_digits=5, decimal_places=2)
    semaforo = models.CharField(max_length=8)
    fecha_calculo = models.DateTimeField()
    meta_id_meta = models.ForeignKey('Meta', models.DO_NOTHING, db_column='Meta_id_meta')  

    def __str__(self):
        return f"Indicador {self.id_indicador} - {self.semaforo}"
    
    class Meta:
        managed = False
        db_table = 'indicador'


class CatalagoItem(models.Model):
    id_item = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=45)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        managed = False
        db_table = 'catalago_item'

class Evidencia(models.Model):
    id_evidencia = models.AutoField(primary_key=True)
    archivo_vinculo = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    metadatos = models.JSONField()
    estado_revision = models.CharField(max_length=9)
    id_actividad = models.ForeignKey('Actividad', models.DO_NOTHING, db_column='id_actividad')
    id_funcionario_carga = models.ForeignKey('funcionarioApp.Funcionario', models.DO_NOTHING, db_column='id_funcionario_carga')

    def __str__(self):
        return f"Evidencia {self.id_evidencia} ({self.estado_revision})"

    class Meta:
        managed = False
        db_table = 'evidencia'

class Validacion(models.Model):
    id_validacion = models.IntegerField(primary_key=True)
    decision = models.CharField(max_length=17)
    fecha = models.DateTimeField()
    observacion = models.TextField(blank=True, null=True)
    resultado = models.CharField(max_length=100)
    version = models.IntegerField()
    id_evidencia = models.ForeignKey('Evidencia', models.DO_NOTHING, db_column='id_evidencia')
    id_validador = models.ForeignKey('funcionarioApp.Funcionario', models.DO_NOTHING, db_column='id_validador')

    def __str__(self):
        return f"Validación {self.id_validacion} ({self.decision})"

    class Meta:
        managed = False
        db_table = 'validacion'
