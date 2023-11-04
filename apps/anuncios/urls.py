from django.urls import path
from .views import ListadoAnuncios, ListadoAnuncioAdmin, RegistrarAnuncio

APP_NAME = 'anuncio'

urlpatterns = [
    path('listado-de-anuncios/', ListadoAnuncioAdmin.as_view(), name='listado_anuncios_admin' ),
    path('anuncios/', ListadoAnuncios.as_view(), name='listado_anuncios' ),
    path('registrar-anuncio/', RegistrarAnuncio.as_view(), name='registrar_anuncio' ),
]
