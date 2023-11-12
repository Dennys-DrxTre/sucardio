from django.urls import path
from .views import (
	UserLoginView, 
	SearchView,
	ListadoUsuarios,
	ChangePassword
)

APP_NAME = 'usuarios'

urlpatterns = [
	path('ingresar/', UserLoginView.as_view(), name='ingresar'),
	path('cambiar-clave/', ChangePassword.as_view(), name='cambiar_clave'),

	# motor de busqueda
	path('search/', SearchView.as_view(), name='search'),

	# listado de usuarios
	path('listado-de-usuarios/', ListadoUsuarios.as_view(), name='listado_usuarios'),
]
