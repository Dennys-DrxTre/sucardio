from django.urls import path
from apps.citas.views.medico.views import (
    ListadoMedico,
    RegistrarMedico,
    EditarMedico,
    DetalleMedico,
    CambiarEstadoMedico
)

APP_NAME = 'citas'

urlpatterns = [
    path('listado-de-medicos/', ListadoMedico.as_view(), name='listado_medico'),
    path('registrar-medico/', RegistrarMedico.as_view(), name='registrar_medico'),
    path('editar-medico/<int:pk>/', EditarMedico.as_view(), name='editar_medico'),
    path('cambiar-estado-medico/<int:pk>/', CambiarEstadoMedico.as_view(), name='cambiar_estado_medico'),
    path('detalle-del-medico/<int:pk>/', DetalleMedico.as_view(), name='detalle_medico'),
]
