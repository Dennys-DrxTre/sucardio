from django import template
from ..models import Notificacion

register = template.Library()

@register.simple_tag
def get_notifications(user):
    data = {}
    query = Notificacion.objects.filter(user__cedula=user.username, leido=False)
    cantidad_de_notificaciones = query.count()
    
    data['notificaciones'] = query
    data['count'] = cantidad_de_notificaciones
    return data