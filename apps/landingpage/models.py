from django.db import models
from apps.citas.models import ModeloBaseEstado

# Create your models here.

class LandingPage(models.Model):
	nombre = models.CharField(max_length=50, null=False, blank=False)
	historia = models.TextField(null=True, blank=True)
	mision = models.TextField(null=True, blank=True)
	vision = models.TextField(null=True, blank=True)
	descripcion = models.TextField(null=True, blank=True)
	
	# contacto
	direccion = models.CharField(max_length=80, null=True, blank=True)
	telefono = models.CharField(max_length=11, null=True, blank=True)
	telefono2 = models.CharField(max_length=11, null=True, blank=True)
	telefono3 = models.CharField(max_length=11, null=True, blank=True)
	telefono4 = models.CharField(max_length=11, null=True, blank=True)

	whatsapp = models.URLField(max_length=150, null=True, blank=True)
	instagram = models.URLField(max_length=150, null=True, blank=True)
	instagram2 = models.URLField(max_length=150, null=True, blank=True)
	instagram3 = models.URLField(max_length=150, null=True, blank=True)
	instagram4 = models.URLField(max_length=150, null=True, blank=True)
	instagram5 = models.URLField(max_length=150, null=True, blank=True)

	facebook = models.URLField(max_length=150, null=True, blank=True)
	email = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.nombre
	
	class Meta:
		permissions = []
		verbose_name = 'Landing Page'
		verbose_name_plural = 'Landing Page'
