from django.db import models
from apps.citas.models import Usuario, ModeloBaseEstado
from .choices import metodos_pago
from datetime import date
# Create your models here.

class Servicio(ModeloBaseEstado):
	nombre_serv = models.CharField(max_length=50, null=False, blank=False)
	descripcion = models.TextField(null=True, blank=True)
	precio_serv = models.FloatField(default=0.00, null=False, blank=False)
	medico = models.ForeignKey(Usuario, on_delete=models.PROTECT)

	def __str__(self):
		return self.nombre_serv
	
	class Meta:
		permissions = []
		verbose_name = 'Servicio'
		verbose_name_plural = 'Servicios'

class Presupuesto(ModeloBaseEstado):
	cliente = models.ForeignKey(Usuario, on_delete=models.PROTECT)
	metodo_pago = models.CharField(max_length=50, choices=metodos_pago, null=False, blank=False, default='Pago móvil')
	total = models.FloatField(default=0.00, null=True, blank=True)
	fecha = models.DateField(auto_now=False, auto_now_add=False, default=date.today, null=True, blank=True)
	servicio = models.ManyToManyField(Servicio)

	def __str__(self):
		return str(self.id) + ' - ' + str(self.fecha)
	
	class Meta:
		permissions = []
		verbose_name = 'Presupuesto'
		verbose_name_plural = 'Presupuestos'