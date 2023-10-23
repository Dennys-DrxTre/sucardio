from django.db import models

class Personal(models.Model):
    cedula = models.CharField(max_length=8)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_ingreso = models.DateField(auto_created=False, auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.cedula
    
    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'

# Create your models here.
class Anuncios(models.Model):
    fecha_publicacion = models.DateField(auto_created=True, auto_now=True, null=True, blank=True)
    fecha_actualizacion = models.DateField(auto_created=True, auto_now=True, null=True, blank=True)
    titulo = models.CharField(max_length=150, null=True, blank=True)
    imagen = models.ImageField(upload_to="anuncios", null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    autor = models.ForeignKey(Personal, on_delete=models.PROTECT, blank=False, null=False)

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name = 'Anuncio'
        verbose_name_plural = 'Anuncios'