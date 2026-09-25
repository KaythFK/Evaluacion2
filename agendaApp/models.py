from django.db import models

# Create your models here.
class Compromiso(models.Model):
    id_compromiso = models.AutoField(primary_key=True)
    origen = models.CharField(max_length=100)
    solicitante = models.CharField(max_length=150)
    territorio = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField()
    fecha_comprometida = models.DateField()
    fecha_termino = models.DateField(blank=True, null=True)
    apoyo = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=12)
    id_funcionario = models.ForeignKey('funcionarioApp.Funcionario', models.DO_NOTHING, db_column='id_funcionario')

    def __str__(self):
        return f"Compromiso {self.id_compromiso} - {self.solicitante}"

    class Meta:
        managed = False
        db_table = 'compromiso'


class ObservacionCompromiso(models.Model):
    id_observacioncomp = models.AutoField(primary_key=True)
    texto = models.TextField()
    fecha = models.DateTimeField()
    id_compromiso = models.ForeignKey('Compromiso', models.DO_NOTHING, db_column='id_compromiso')

    def __str__(self):
        return f"Observación {self.id_observacioncomp}"

    class Meta:
        managed = False
        db_table = 'observacion_compromiso'