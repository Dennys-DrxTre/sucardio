from django.db import models
from apps.citas.models import Usuario, ModeloBaseEstado, Medico
from .choices import metodos_pago
from datetime import date, timedelta
from django.urls import reverse
from django.forms import model_to_dict

# Create your models here.

def obtener_fecha_vencimiento():
    return date.today() + timedelta(days=15)

class Servicio(ModeloBaseEstado):
	nombre_serv = models.CharField(max_length=50, null=False, blank=False)
	descripcion = models.TextField(null=True, blank=True)
	precio_serv = models.FloatField(default=0.00, null=False, blank=False)
	medico = models.ForeignKey(Medico, on_delete=models.PROTECT)

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
	fecha_vencimiento = models.DateField(auto_now=False, auto_now_add=False, default=obtener_fecha_vencimiento, null=True, blank=True)
	servicio = models.ManyToManyField(Servicio)

	def __str__(self):
		return str(self.id) + ' - ' + str(self.fecha)
	
	def toJSON(self):
		item = model_to_dict(self)
		item['model'] = 'Presupuesto'
		item['servicio'] = ''
		item['url'] = self.get_absolute_url()
		item['cliente'] = {'pk':self.cliente.pk, 'cedula':self.cliente.cedula, 'nombre':self.cliente.nombre, 'apellido':self.cliente.apellido}
		item['fecha'] = date.strftime(self.fecha, '%d/%m/%Y')
		item['fecha_vencimiento'] = date.strftime(self.fecha_vencimiento, '%d/%m/%Y')
		return item

	def get_absolute_url(self):
		return reverse('detalle_presupuesto', args=[self.id])

	def get_model_name(self):
		return 'Presupuesto'

	class Meta:
		permissions = []
		verbose_name = 'Presupuesto'
		verbose_name_plural = 'Presupuestos'