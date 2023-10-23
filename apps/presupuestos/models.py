from django.db import models
from apps.citas.models import Usuario
# Create your models here.

class Servicio(models.Model):
    nombre_serv = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    precio_serv = models.FloatField(default=0.00, null=False, blank=False)
    metodo_pago = models.CharField(max_length=20, null=False, blank=False)
    medico = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

class Presupuesto(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name = 'Presupuesto'
        verbose_name_plural = 'Presupuestos'