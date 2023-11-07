from django.urls import path
from apps.citas.views.medico.views import (
    ListadoMedico,
    RegistrarMedico,
    EditarMedico,
    DetalleMedico,
    CambiarEstadoMedico,
)

from apps.citas.views.citas.views import (
    ListadoCita,
    DetallesCita,
    EditarCita,
)

APP_NAME = 'citas'

urlpatterns = [
    path('listado-de-medicos/', ListadoMedico.as_view(), name='listado_medico'),
    path('registrar-medico/', RegistrarMedico.as_view(), name='registrar_medico'),
    path('editar-medico/<int:pk>/', EditarMedico.as_view(), name='editar_medico'),
    path('cambiar-estado-medico/<int:pk>/', CambiarEstadoMedico.as_view(), name='cambiar_estado_medico'),
    path('detalle-del-medico/<int:pk>/', DetalleMedico.as_view(), name='detalle_medico'),

    #citas
    path('listado-de-citas/', ListadoCita.as_view(), name='listado_citas'),
    path('detalle-de-citas/<int:pk>/', DetallesCita.as_view(), name='detalle_cita'),
    path('editar-cita/<int:pk>/', EditarCita.as_view(), name='editar_cita'),
]
