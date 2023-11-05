from django.urls import path
from .views import ListadoAnuncios, ListadoAnuncioAdmin, RegistrarAnuncio, EditarAnuncio, CambiarEstadoAnuncio, DetalleAnuncio, DetalleAnuncioLanding

APP_NAME = 'anuncio'

urlpatterns = [
    path('listado-de-anuncios/', ListadoAnuncioAdmin.as_view(), name='listado_anuncios_admin' ),
    path('anuncios/', ListadoAnuncios.as_view(), name='listado_anuncios' ),
    path('registrar-anuncio/', RegistrarAnuncio.as_view(), name='registrar_anuncio' ),
    path('editar-anuncio/<int:pk>/', EditarAnuncio.as_view(), name='editar_anuncio' ),
    path('detalles-del-anuncio/<int:pk>/', DetalleAnuncio.as_view(), name='detalle_anuncio' ),
    path('anuncio/<int:pk>/', DetalleAnuncioLanding.as_view(), name='detalle_anuncio_landing' ),
    path('cambiar-estado-anuncio/<int:pk>/', CambiarEstadoAnuncio.as_view(), name='cambiar_estado_anuncio' ),
]
