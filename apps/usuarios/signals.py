from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Notificacion
from apps.citas.models import Cita

@receiver(post_save, sender=Cita)
def cambiar_estado_cita(sender, instance, **kwargs):
    mensaje = {
        'AP': f'su cita con ID:{instance.pk} ha sido aprobado',
        'RE': f'su cita con ID:{instance.pk} ha sido rechazado'
    }
    if not instance.notificado:
        if not instance.estado == 'PE':
            notificacion = Notificacion()
            notificacion.titulo = mensaje[instance.estado]
            notificacion.user = instance.cliente
            notificacion.cita = instance
            notificacion.save()
            instance.notificado = True
            instance.save()
