from django.urls import path
from apps.presupuestos.views.servicios.views import (
    ListadoServicio, 
    RegistrarServicio, 
    EditarServicio, 
    DetalleServicio,
    CambiarEstadoServicio
)

from apps.presupuestos.views.presupuestos.views import (
    ListadoPresupuesto,
    RegistrarPresupuesto
)

APP_NAME = 'presupuestos'

urlpatterns = [
    # SERVICIOS
    path('listado-de-servicios/', ListadoServicio.as_view(), name='listado_servicios'),
    path('registrar-servicio/', RegistrarServicio.as_view(), name='registrar_servicio'),
    path('actualizar-servicio/<int:pk>/', EditarServicio.as_view(), name='editar_servicio'),
    path('detalle-servicio/<int:pk>/', DetalleServicio.as_view(), name='detalle_servicio'),
    path('cambiar-estado-servicio/<int:pk>/', CambiarEstadoServicio.as_view(), name='cambiar_estado_servicio'),

    # PRESUPUESTO
    path('listado-de-presupuestos/', ListadoPresupuesto.as_view(), name='listado_presupuestos'),
    path('registrar-presupuesto/', RegistrarPresupuesto.as_view(), name='registrar_presupuesto'),

]
