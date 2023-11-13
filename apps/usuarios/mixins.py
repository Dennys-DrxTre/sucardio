from django.shortcuts import redirect
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

class ValidarUsuario(LoginRequiredMixin, UserPassesTestMixin):
	permission_required = None
	redirect_url = '/acceso-denegado/'

	def test_func(self):
		return self.request.user.has_perm(self.permission_required)

	def handle_no_permission(self):
		if not self.request.user.has_perm(self.permission_required):
			return redirect(self.redirect_url)

		return super().handle_no_permission()

	def dispatch(self, request, *args, **kwargs):
		if not self.request.user.is_authenticated:
			return redirect('/ingresar/')
		return super().dispatch(request, *args, **kwargs)

# class Perms_Check(LoginRequiredMixin, PermissionRequiredMixin):
# 	permission_required = ''
# 	url_redirect = '/'

# 	def get_perms(self):
# 		if isinstance(self.permission_required, str):
# 			perms = (self.permission_required,)
# 		else:
# 			perms = self.permission_required
# 		return perms

# 	def handle_no_permission(self):
# 		print(self.request.user.has_perm('anuncios.requiere_usuario',))
# 		if self.request.user.has_perm('anuncios.requiere_usuario',):
# 			print('hola')
# 			self.url_redirect = '/'
# 		elif self.request.user.has_perm('anuncios.requiere_secretaria',):
# 			print('hola 2')
# 			self.url_redirect = 'listados_citas'
# 		elif self.request.user.has_perm('anuncios.requiere_admin',):
# 			print('hola 3')
# 			self.url_redirect = 'listados_citas'
# 		messages.error(self.request, 'No tiene permisos para ingresar a este modulo')
# 		print('x')
# 		return redirect(self.url_redirect)

# 	def dispatch(self, request,*args, **kwargs):
# 		if request.user.has_perms(self.get_perms()):
# 			return super().dispatch(request, *args, **kwargs)
# 		return self.handle_no_permission()