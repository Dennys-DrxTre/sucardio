from django.urls import path
from .views import ReportePrueba

APP_NAME = 'reportes'

urlpatterns = [
    # PRUEBA
    path('prueba/', ReportePrueba.as_view(), name='prueba'),

]
