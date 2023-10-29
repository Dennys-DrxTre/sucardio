from multiselectfield import MultiSelectField

from django.db import models
from apps.anuncios.models import Usuario, Persona, ModeloBaseEstado
from .choices import especialidades

class Medico(Persona):

	class Estado(models.TextChoices):
		HABILITADO = 'AC', 'Habilitado'
		DESHABILITADO = 'DE', 'Deshabilitado'

	estado = models.CharField(max_length=2, choices=Estado.choices, default=Estado.HABILITADO, null=True, blank=True)
	fecha_ingreso = models.DateField(auto_created=False, auto_now=False, null=True, blank=True)
	especialidad = MultiSelectField(choices=especialidades)
	horario_inicio = models.TimeField(null=True, blank=True)
	horario_final = models.TimeField(null=True, blank=True)

	def __str__(self):
		return self.cedula
	
	class Meta:
		permissions = []
		verbose_name = 'Medico'
		verbose_name_plural = 'Medicos'

class Cita(ModeloBaseEstado):
	control_pac = models.BooleanField(default=False)
	fecha_cita = models.DateField(auto_created=False, auto_now=False, null=True, blank=True)
	motivo_consulta = models.TextField(null=False, blank=False)
	metodo_pago = models.CharField(max_length=20, null=False, blank=False)
	medico = models.ForeignKey(Medico ,on_delete=models.PROTECT, blank=False, null=False)

	def __str__(self):
		return self.id
	
	class Meta:
		permissions = []
		verbose_name = 'Cita'
		verbose_name_plural = 'Citas'