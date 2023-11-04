from django.urls import path
from .views import Inicio, MisCitas, SolicitarCita, DetalleMiCita, Anuncios, Contacto

APP_NAME = 'landingpage'

urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    path('mis-citas/', MisCitas.as_view(), name='mis_citas'),
    path('solicitar-cita/', SolicitarCita.as_view(), name='registrar_cita_cliente'),
    path('detalle-de-mi-cita/<int:pk>/', DetalleMiCita.as_view(), name='registrar_cita_cliente'),
    path('anuncios/', Anuncios.as_view(), name='anuncios'),
    path('contactanos/', Contacto.as_view(), name='contactanos'),
]