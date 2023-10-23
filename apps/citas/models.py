from django.db import models
from apps.anuncios.models import Usuario


class Cita(models.Model):
    control_pac = models.BooleanField(default=False)
    fecha_cita = models.DateField(auto_created=False, auto_now=False, null=True, blank=True)
    motivo_consulta = models.TextField(null=False, blank=False)
    metodo_pago = models.CharField(max_length=20, null=False, blank=False)
    medico = models.ForeignKey(Usuario ,on_delete=models.PROTECT, blank=False, null=False)

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'