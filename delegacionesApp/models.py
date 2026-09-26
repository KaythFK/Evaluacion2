from django.db import models

class Delegacion(models.Model):
    id_delegacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    responsable = models.IntegerField(blank=True, null=True)
    territorio = models.CharField(max_length=45, blank=True, null=True)
    calle = models.CharField(max_length=60, blank=True, null=True)
    numero_calle = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delegacion'

    def __str__(self):
        return str(self.nombre)