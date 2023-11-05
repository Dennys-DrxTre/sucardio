from django.urls import path
from apps.presupuestos.views.servicios.views import ListadoServicio

APP_NAME = 'presupuestos'

urlpatterns = [
    path('listado-de-servicios/', ListadoServicio.as_view(), name='listado_servicios'),
]
