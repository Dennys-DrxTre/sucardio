from django.db import models
from apps.anuncios.models import Usuario, Persona, ModeloBaseEstado
from .choices import especialidades
from apps.presupuestos.choices import metodos_pago
from django.urls import reverse
from django.forms import model_to_dict
from datetime import date

class Medico(Persona):

	class Estado(models.TextChoices):
		HABILITADO = 'AC', 'Habilitado'
		DESHABILITADO = 'DE', 'Deshabilitado'

	estado = models.CharField(max_length=2, choices=Estado.choices, default=Estado.HABILITADO, null=True, blank=True)
	fecha_ingreso = models.DateField(auto_created=False, auto_now=False, null=True, blank=True)
	especialidad = models.CharField(max_length=100, choices=especialidades,null=False, blank=False)
	horario_inicio = models.TimeField(null=True, blank=True)
	horario_final = models.TimeField(null=True, blank=True)

	def __str__(self):
		return str(f'{self.nombre} {self.apellido} | {self.especialidad}')
	
	def toJSON(self):
		item = model_to_dict(self)
		item['model'] = 'Medico'
		item['url'] = self.get_absolute_url()
		item['fecha_ingreso'] = date.strftime(self.fecha_ingreso, '%d/%m/%Y')
		return item

	def get_absolute_url(self):
		return reverse('detalle_medico', args=[self.id])

	def get_model_name(self):
		return 'Medico'

	class Meta:
		permissions = []
		verbose_name = 'Medico'
		verbose_name_plural = 'Medicos'

class Cita(ModeloBaseEstado):

	class Estado(models.TextChoices):
		PENDIENTE = 'PE', 'Pendiente'
		APROBADO = 'AP', 'Aprobado'
		RECHAZADO = 'RE', 'Rechazado'

	control_pac = models.BooleanField(default=False)
	fecha_cita = models.DateField(auto_created=False, auto_now=False, null=True, blank=True)
	motivo_consulta = models.TextField(null=False, blank=False)
	metodo_pago = models.CharField(max_length=30, null=False, blank=False, choices=metodos_pago)
	estado = models.CharField(max_length=20, null=False, blank=False, choices=Estado.choices, default=Estado.PENDIENTE)
	cliente = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=False, blank=False)
	medico = models.ForeignKey(Medico ,on_delete=models.PROTECT, blank=False, null=False)

	def __str__(self):
		return str(self.id)

	def toJSON(self):
		item = model_to_dict(self)
		item['model'] = 'Cita'
		item['url'] = self.get_absolute_url()
		item['medico'] = {'pk':self.medico.pk, 'cedula':self.medico.cedula, 'nombre':self.medico.nombre, 'apellido':self.medico.apellido}
		item['cliente'] = {'pk':self.cliente.pk, 'cedula':self.cliente.cedula, 'nombre':self.cliente.nombre, 'apellido':self.cliente.apellido}
		if self.fecha_cita:
			item['fecha_cita'] = date.strftime(self.fecha_cita, '%d/%m/%Y')
		return item

	def get_absolute_url(self):
		return reverse('detalle_cita', args=[self.id])

	def get_model_name(self):
		return 'Cita'

	class Meta:
		permissions = []
		verbose_name = 'Cita'
		verbose_name_plural = 'Citas'