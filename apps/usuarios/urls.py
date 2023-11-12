from django.urls import path
from .views import (
    UserLoginView, 
    SearchView,
    ListadoUsuarios,
    DetalleUsuario,
    RegistrarUsuario,
    EditarUsuario,
    EditarContrasenaUsuario,
    CambiarEstadoUsuario
)

APP_NAME = 'usuarios'

urlpatterns = [
    path('ingresar/', UserLoginView.as_view(), name='ingresar'),

    # motor de busqueda
    path('search/', SearchView.as_view(), name='search'),

    # listado de usuarios
    path('listado-de-usuarios/', ListadoUsuarios.as_view(), name='listado_usuarios'),
    path('detalle-de-usuario/<int:pk>/', DetalleUsuario.as_view(), name='detalle_usuario'),
    path('registrar-usuario/', RegistrarUsuario.as_view(), name='registrar_usuario'),
    path('editar-usuario/<int:pk>/', EditarUsuario.as_view(), name='editar_usuario'),
    path('editar-contrasena-usuario/<int:pk>/', EditarContrasenaUsuario.as_view(), name='editar_contrasena_usuario'),
    path('cambiar-estado-usuario/<int:pk>/', CambiarEstadoUsuario.as_view(), name='cambiar_estado_usuario'),
]
