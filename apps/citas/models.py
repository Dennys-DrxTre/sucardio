from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    # DATOS GENERALES
    nombre_pac = models.CharField(max_length=50, null=False, blank=False)
    apellido_pac = models.CharField(max_length=50, null=False, blank=False)
    cedula_pac = models.CharField(max_length=10, null=False, blank=False)
    telefono = models.CharField(max_length=16, null=False, blank=False)
    telefono2 = models.CharField(max_length=16, null=True, blank=True)
    direccion = models.TextField(null=False, blank=False)

    # DATOS DEL MEDICO
    profesion = models.CharField(max_length=100, null=True, blank=True)
    especialidad = models.CharField(max_length=100, null=True, blank=True)
    horario = models.CharField(max_length=150, null=True, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.cedula_pac
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

# Create your models here.
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