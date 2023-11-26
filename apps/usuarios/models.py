from datetime import date

from django.db import models
from apps.anuncios.models import Usuario
from apps.citas.models import Cita
from django.forms import model_to_dict
from datetime import datetime
from django.urls import reverse

# Create your models here.

class Notificacion(models.Model):
    titulo = models.CharField(max_length=50)
    leido = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_created=True, default=datetime.now)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)

    def toJSON(self):
        item = model_to_dict(self)
        item['url'] = self.cita.get_absolute_url()
        item['fecha'] = date.strftime(self.fecha, '%d/%m/%Y')
        return item

    def get_absolute_url(self):
        return reverse('verificar-notificacion', args=[self.id])

    def __str__(self):
        return str(f'{self.pk} | {self.fecha}')