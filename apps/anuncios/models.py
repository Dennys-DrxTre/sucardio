from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Persona(models.Model):

	# DATOS GENERALES
	nombre = models.CharField(max_length=50, null=False, blank=False)
	apellido = models.CharField(max_length=50, null=False, blank=False)
	cedula = models.CharField(max_length=10, null=False, blank=False)
	telefono = models.CharField(max_length=11, null=False, blank=False)
	telefono2 = models.CharField(max_length=11, null=True, blank=True)
	direccion = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.cedula

	class Meta:
		abstract = True

class ModeloBaseEstado(models.Model):

	class Estado(models.TextChoices):
		HABILITADO = 'AC', 'Habilitado'
		DESABILITADO = 'DE', 'Desabilitado'

	estado = models.CharField(max_length=2, choices=Estado.choices, default=Estado.HABILITADO, null=True, blank=True)

	def __str__(self):
		return self.pk

	class Meta:
		abstract = True

class Usuario(Persona):

	class Permission(models.TextChoices):
		ADMIN = 'AD', 'Admin'
		SECRETARIA = 'SE', 'Secretaria'
		CLIENTE = 'CL', 'Cliente'

	fecha_registro = models.DateField(auto_created=True, null=True, blank=True)
	tipo_usuario = models.CharField(max_length=2, choices=Permission.choices, default=Permission.CLIENTE)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return str(f'{self.cedula} | {self.nombre} | {self.apellido}')

	def get_absolute_url(self):
		return reverse('detalle_usuario', args=[self.id])

	def get_model_name(self):
		return 'Usuario'
	
	def get_user(self):
		user = User.objects.filter(username=self.cedula).exists()
		if user:
			return User.objects.get(username=self.cedula)
		return None

	class Meta:
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'
		permissions = [
			('requiere_usuario', 'requiero nivel usuario'),
			('requiere_secretria', 'requiero nivel secretaria'),
			('requiere_admin', 'requiero nivel admin')
		]

class Anuncios(ModeloBaseEstado):
	fecha_publicacion = models.DateField(auto_created=True, auto_now=True, null=True, blank=True)
	fecha_actualizacion = models.DateField(auto_created=True, auto_now=True, null=True, blank=True)
	titulo = models.CharField(max_length=150, null=True, blank=True)
	imagen = models.ImageField(upload_to="anuncios", null=True, blank=True)
	descripcion = models.TextField(null=True, blank=True)
	autor = models.ForeignKey(Usuario, on_delete=models.PROTECT, blank=False, null=False)

	def __str__(self):
		return self.titulo
	
	def get_absolute_url(self):
		return reverse('detalle_anuncio', args=[self.id])

	def get_model_name(self):
		return 'Anuncio'

	class Meta:
		permissions = []
		verbose_name = 'Anuncio'
		verbose_name_plural = 'Anuncios'