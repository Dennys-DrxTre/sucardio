from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):

	class Permission(models.TextChoices):
		ADMIN = 'AD', 'Admin'
		MEDICO = 'ME', 'Medico'
		CLIENTE = 'CL', 'Cliente'

	# DATOS GENERALES
	nombre = models.CharField(max_length=50, null=False, blank=False)
	apellido = models.CharField(max_length=50, null=False, blank=False)
	cedula = models.CharField(max_length=10, null=False, blank=False)
	telefono = models.CharField(max_length=16, null=False, blank=False)
	telefono2 = models.CharField(max_length=16, null=True, blank=True)
	direccion = models.TextField(null=True, blank=True)

	# DATOS PERSONAL
	cargo = models.CharField(max_length=100, null=True, blank=True)
	fecha_ingreso = models.DateField(auto_created=False, auto_now=False, null=True, blank=True)

	# DATOS DEL MEDICO
	especialidad = models.CharField(max_length=100, null=True, blank=True)
	horario_inicio = models.TimeField(null=True, blank=True)
	horario_final = models.TimeField(null=True, blank=True)

	tipo_usuario = models.CharField(max_length=2, choices=Permission.choices, default=Permission.CLIENTE)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.cedula
	
	class Meta:
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'

class Anuncios(models.Model):
	fecha_publicacion = models.DateField(auto_created=True, auto_now=True, null=True, blank=True)
	fecha_actualizacion = models.DateField(auto_created=True, auto_now=True, null=True, blank=True)
	titulo = models.CharField(max_length=150, null=True, blank=True)
	imagen = models.ImageField(upload_to="anuncios", null=True, blank=True)
	descripcion = models.TextField(null=True, blank=True)
	autor = models.ForeignKey(Usuario, on_delete=models.PROTECT, blank=False, null=False)

	def __str__(self):
		return self.id
	
	class Meta:
		verbose_name = 'Anuncio'
		verbose_name_plural = 'Anuncios'