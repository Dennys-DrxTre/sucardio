from django.urls import path
from .views.citas.views import DetalleCita, CitasDelDia, DetalleMiCita, TodasLasCitas
from .views.medicos.views import ReporteMedicos,ReporteDetalleMedico
from .views.usuarios.views import ReporteUsuarios, ReporteDetalleUsuario
from .views.presupuesto.views import ReportePresupuestos, ReporteDetallePresupuesto,ReporteDetalleMiPresupuesto

APP_NAME = 'reportes'

urlpatterns = [
    path('listado-de-citas/', TodasLasCitas.as_view(), name='todas_citas'),
    path('detalle-de-cita/<int:pk>/', DetalleCita.as_view(), name='det_cita'),
    path('detalle-de-mi-cita/<int:pk>/', DetalleMiCita.as_view(), name='det_mi_cita'),
    path('citas-del-dia/<int:pk>/', CitasDelDia.as_view(), name='citas_dia'),
    # MEDICOS
    path('listado-de-medicos/', ReporteMedicos.as_view(), name='reporte_medicos'),
    path('detalle-de-medico/<int:pk>/', ReporteDetalleMedico.as_view(), name='reporte_detalle_medico'),
    # USUARIOS
    path('listado-de-usuarios/', ReporteUsuarios.as_view(), name='reporte_usuarios'),
    path('detalle-de-usuario/<int:pk>/', ReporteDetalleUsuario.as_view(), name='reporte_detalle_usuario'),
    # PRESUPUESTO
    path('listado-de-presupuestos/', ReportePresupuestos.as_view(), name='reporte_presupuestos'),
    path('detalle-de-presupuesto/<int:pk>/', ReporteDetallePresupuesto.as_view(), name='reporte_detalle_presupuesto'),
    path('detalle-de-mi-presupuesto/<int:pk>/', ReporteDetalleMiPresupuesto.as_view(), name='reporte_detalle_mi_presupuesto'),
]
