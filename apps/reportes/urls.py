from django.urls import path
from .views import ReportePrueba, DetalleCita, CitasDelDia

APP_NAME = 'reportes'

urlpatterns = [
    # PRUEBA
    path('prueba/', ReportePrueba.as_view(), name='prueba'),
    path('detalle-de-cita/<int:pk>/', DetalleCita.as_view(), name='det_cita'),
    path('citas-del-dia/<int:pk>/', CitasDelDia.as_view(), name='citas_dia'),
]
