from django.urls import path
from apps.anuncios.views.personal.views import (
    ListadoPersonal,
    RegistrarPersonal
)

APP_NAME = 'anuncio'

urlpatterns = [

    path('listado-de-personal/', ListadoPersonal.as_view(), name='listado_personal'),
    path('registrar-personal/', RegistrarPersonal.as_view(), name='registrar_personal'),
]
