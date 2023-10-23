from django.urls import path
from apps.anuncios.views.personal.views import (
    ListadoPersonal
)

APP_NAME = 'anuncio'

urlpatterns = [

    path('listado-de-personal/', ListadoPersonal.as_view(), name='listado_personal'),
]
