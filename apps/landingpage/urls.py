from django.urls import path
from .views import (
    Inicio, 
    MisCitas, 
    RegistrarCita, 
    DetalleMiCita, 
    Contacto, 
    SobreNosotros, 
    ListadoMiPresupuesto, 
    DetalleMiPresupuesto,
    RegistrarMiPresupuesto,
    MiPerfil
)

APP_NAME = 'landingpage'

urlpatterns = [
    path('', Inicio.as_view(), name='inicio_front'),
    path('mis-citas/', MisCitas.as_view(), name='mis_citas'),
    path('solicitar-cita/', RegistrarCita.as_view(), name='registrar_cita_cliente'),
    path('detalle-de-mi-cita/<int:pk>/', DetalleMiCita.as_view(), name='detalle_cita_cliente'),
    path('contactanos/', Contacto.as_view(), name='contactanos'),
    path('quienes-somos/', SobreNosotros.as_view(), name='sobre_nosotros'),

    # presupuesto
    path('registrar-mi-presupuesto/', RegistrarMiPresupuesto.as_view(), name='registrar_mi_presupuesto'),
    path('mi-presupuesto/', ListadoMiPresupuesto.as_view(), name='mi_presupuesto'),
    path('detalle-de-mi-presupuesto/<int:pk>/', DetalleMiPresupuesto.as_view(), name='detalle_mi_presupuesto'),

    # Mi Perfil
    path('mi-perfil/', MiPerfil.as_view(), name='mi_perfil'),
]