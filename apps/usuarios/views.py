from itertools import chain
from datetime import date

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, DetailView, UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse

from apps.citas.models import Medico, Cita
from apps.presupuestos.models import Presupuesto
from apps.anuncios.models import Anuncios, Usuario
from django.contrib.auth.models import User, Permission
from .perms import permissions_user

from .mixins import ValidarUsuario

from .forms import LoginForm, SearchForm, RegistrarUsuarioAdmin, EditarUsuarioAdmin, EditarPasswordUsuarioForm,ChangePass

class UserLoginView(TemplateView):
	template_name = 'registration/login.html'

	def post(self, request, *args, **kwargs):
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/') # redirige al usuario a la página de inicio después de iniciar sesión
			else:
				messages.error(request, 'Usuario o contraseña incorrecta.')
		else:
			messages.error(request, 'Por favor, introduce un nombre de usuario y contraseña válidos.')
		return render(request, self.template_name, {'form': form})

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['sub_title'] = "Ingresar"
		context['form'] = LoginForm()
		return context

class ChangePassword(ValidarUsuario, TemplateView):
	template_name = 'registration/cambiar_clave.html'
	permission_required = 'anuncios.requiere_usuario'

	def get_form(self, request):
		return ChangePass(request.POST or None)

	def post(self, request, *args, **kwargs):
		form = self.get_form(request)
		if form.is_valid():
			pass_actual = form.cleaned_data.get('pass_actual')
			pass1 = form.cleaned_data.get('nueva_pas1')
			pass2 = form.cleaned_data.get('nueva_pas2')
			user = authenticate(username=request.user.username, password=pass_actual)
			if pass1 != pass2:
				messages.error(request, 'La nueva contraseña no coincide, intenta de nuevo.')
			elif user is not None:
				user.set_password(pass1)
				user.save()
				messages.success(request, 'Contraseña actualizada correctamente.')  # Mensaje antes de cerrar sesión
				logout(request)
				return redirect('/ingresar/')
			else:
				messages.error(request, 'Contraseña actual incorrecta.')
		else:
			messages.error(request, 'Por favor, introduce una contaseña válida.')
		return render(request, self.template_name, {'form': form})
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['sub_title'] = "Cambiar clave"
		context['form'] = self.get_form(self.request)
		return context

class SearchView(ValidarUsuario, View):
	template_name = 'base/search.html'
	permission_required = 'anuncios.requiere_secretria'
	form_class = SearchForm

	def get(self, request, *args, **kwargs):
		context = {}
		context['sub_title'] = 'Resultados de busquedas'
		context['title'] = 'Buscador'

		form = self.form_class(request.GET)
		if form.is_valid():
			query = form.cleaned_data['search']
			medicos = Medico.objects.filter(
				Q(cedula__icontains=query) | 
				Q(nombre__icontains=query)| 
				Q(apellido__icontains=query))
			usuarios = Usuario.objects.filter(
				Q(user__username__icontains=query) | 
				Q(nombre__icontains=query))
			citas = Cita.objects.filter(
				Q(id__icontains=query) | 
				Q(medico__nombre__icontains=query)| 
				Q(medico__cedula__icontains=query))
			presupuestos = Presupuesto.objects.filter(
				Q(id__icontains=query) | 
				Q(cliente__cedula__icontains=query)|
				Q(cliente__nombre__icontains=query)|  
				Q(metodo_pago__icontains=query))
			anuncios = Anuncios.objects.filter(
				Q(descripcion__icontains=query) | 
				Q(titulo__icontains=query)| 
				Q(autor__cedula__icontains=query))

			medicos_count = medicos.count()
			usuarios_count = usuarios.count()
			citas_count = citas.count()
			presupuestos_count = presupuestos.count()
			anuncios_count = anuncios.count()
			# combinar los resultados y pasarlos al contexto del template
			results = list(chain(medicos, usuarios, citas, presupuestos, anuncios))
			total_results = medicos_count + usuarios_count + citas_count + presupuestos_count + anuncios_count

			paginator = Paginator(results, 8)  # Muestra 10 resultados por página

			# Obtiene el número de página del parámetro GET 'page'. Si no existe, asume 1.
			page_number = request.GET.get('page', 1)

			try:
				page_obj = paginator.page(page_number)
			except PageNotAnInteger:
				# Si la página no es un entero, muestra la primera página.
				page_obj = paginator.page(1)
			except EmptyPage:
				# Si la página está fuera de rango (por ejemplo, 9999), muestra la última página de resultados.
				page_obj = paginator.page(paginator.num_pages)

			context['results'] = page_obj
			context['total_results'] = total_results
			context['query'] = query
		else:
			results = []
		return render(request, self.template_name, context)

class ListadoUsuarios(ValidarUsuario, TemplateView):
	template_name = 'pages/usuarios/listado_usuarios.html'
	permission_required = 'anuncios.requiere_secretria'
	login_url = '/acceso-denegado/'

	def get(self, request, *args, **kwargs):
		usuarios = Usuario.objects.filter().order_by('cedula')
		filtros = {
			'True': True,
			'False': False,
		}
		search_term = request.GET.get('search', '')
		filter_option = request.GET.get('filtros', 'True')
		context = {}
		context['sub_title'] = 'Listado de usuarios'
		context['title'] = 'Usuarios'

		if search_term or str(filtros[filter_option]):
			usuarios = Usuario.objects.filter(
				Q(user__username__icontains=search_term) | 
				Q(nombre__icontains=search_term) |
				Q(apellido__icontains=search_term),
				user__is_superuser=False,
				user__is_active=filtros[filter_option]
			).order_by('cedula')
		paginator = Paginator(usuarios, 15)  # Muestra 10 resultados por página
		# Obtiene el número de página del parámetro GET 'page'. Si no existe, asume 1.
		page_number = request.GET.get('page', 1)
		try:
			page_obj = paginator.page(page_number)
		except PageNotAnInteger:
			# Si la página no es un entero, muestra la primera página.
			page_obj = paginator.page(1)
		except EmptyPage:
			# Si la página está fuera de rango (por ejemplo, 9999), muestra la última página de resultados.
			page_obj = paginator.page(paginator.num_pages)

		context['results'] = page_obj
		context['filtros'] = filtros[filter_option]
		context['search'] = str(search_term)
		return render(request, self.template_name, context)

class DetalleUsuario(ValidarUsuario, DetailView):
	template_name = 'pages/usuarios/detalle_usuario.html'
	permission_required = 'anuncios.requiere_secretria'
	model = Usuario
	context_object_name = 'usuario'

	def get(self, request, *args, **kwargs):
		usuario_id = self.kwargs.get("pk")
		try:
			self.object = Usuario.objects.get(pk=usuario_id)
		except Usuario.DoesNotExist:
			return redirect('listado_usuarios')
		context = self.get_context_data(object=self.object)
		return self.render_to_response(context)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Usuario"
		context["sub_title"] = "Detalle del usuario"
		return context

class RegistrarUsuario(ValidarUsuario, TemplateView):
	template_name = 'pages/usuarios/registrar_usuario.html'
	permission_required = 'anuncios.requiere_admin'
	object = None

	def get_success_url(self):
		return reverse('detalle_usuario', kwargs={'pk': self.object.pk})

	def post(self, request, *args, **kwargs):
		form = RegistrarUsuarioAdmin(request.POST)
		if form.is_valid():

			user = User()
			user.username = form.cleaned_data['cedula']
			user.first_name = form.cleaned_data['nombre']
			user.last_name = form.cleaned_data['apellido']
			user.set_password(form.cleaned_data['password'])
			user.save()
			permissions = Permission.objects.filter(codename__in=permissions_user[form.cleaned_data['tipo_usuario']])
			for permission in permissions:
				user.user_permissions.add(permission)
			user.save()

			self.object = form.save(commit=False)
			self.object.user = user
			self.object.fecha_registro = date.today()
			self.object.save()

			messages.success(request, 'El usuario se ha registrado correctamente')
			return redirect(self.get_success_url())
		else:
			context = self.get_context_data(**kwargs)
			context["form"] = form
			return render(request, self.template_name, context)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Usuarios"
		context["sub_title"] = "Registrar usuario"
		context["form"] = RegistrarUsuarioAdmin()
		return context

class EditarUsuario(ValidarUsuario, UpdateView):
	template_name = 'pages/usuarios/editar_usuario.html'
	permission_required = 'anuncios.requiere_admin'
	model = Usuario
	form_class = EditarUsuarioAdmin
	object = None

	def get_success_url(self):
		return reverse('detalle_usuario', kwargs={'pk': self.object.pk})

	def get(self, request, *args, **kwargs):
		context = {}
		try:
			self.object = Usuario.objects.get(pk=kwargs['pk'])
			form = EditarUsuarioAdmin(instance=self.object)
			context["title"] = "Usuarios"
			context["sub_title"] = "Editar usuario"
			context["form"] = form
		except Usuario.DoesNotExist:
			return redirect('listado_usuarios')
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		try:
			self.object = Usuario.objects.get(pk=kwargs['pk'])
			form = EditarUsuarioAdmin(request.POST, instance=self.object)
			if form.is_valid():

				user = User.objects.filter(username=self.object.cedula).first()
				user.username = form.cleaned_data['cedula']
				user.first_name = form.cleaned_data['nombre']
				user.last_name = form.cleaned_data['apellido']
				user.user_permissions.clear()
				permissions = Permission.objects.filter(codename__in=permissions_user[form.cleaned_data['tipo_usuario']])
				for permission in permissions:
					user.user_permissions.add(permission)
				user.save()

				self.object = form.save(commit=False)
				self.object.user = user
				self.object.save()

				messages.success(request, 'El usuario se ha editado correctamente')
				return redirect(self.get_success_url())
			else:
				context = self.get_context_data(**kwargs)
				self.object = Usuario.objects.get(pk=kwargs['pk'])
				context["form"] = form
				context["title"] = "Usuarios"
				context["sub_title"] = "Editar usuario"
				return render(request, self.template_name, context)
		except Usuario.DoesNotExist:
			return redirect('listado_usuarios')

class EditarContrasenaUsuario(ValidarUsuario, UpdateView):
	template_name = 'pages/usuarios/editar_contrasena_usuario.html'
	permission_required = 'anuncios.requiere_admin'
	model = Usuario
	form_class = EditarUsuarioAdmin
	object = None

	def get_success_url(self):
		return reverse('detalle_usuario', kwargs={'pk': self.object.pk})

	def get(self, request, *args, **kwargs):
		context = {}
		try:
			self.object = Usuario.objects.get(pk=kwargs['pk'])
			form = EditarPasswordUsuarioForm(instance=self.object)
			context["title"] = "Usuarios"
			context["sub_title"] = "Editar contraseña del usuario"
			context["form"] = form
		except Usuario.DoesNotExist:
			return redirect('listado_usuarios')
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		try:
			self.object = Usuario.objects.get(pk=kwargs['pk'])
			form = EditarPasswordUsuarioForm(request.POST, instance=self.object)
			if form.is_valid():

				user = User.objects.filter(username=self.object.cedula).first()
				user.set_password(form.cleaned_data['password'])
				user.save()

				messages.success(request, 'El usuario se ha editado correctamente')
				return redirect(self.get_success_url())
			else:
				context = self.get_context_data(**kwargs)
				self.object = Usuario.objects.get(pk=kwargs['pk'])
				context["form"] = form
				context["title"] = "Usuarios"
				context["sub_title"] = "Editar contraseña del usuario"
				return render(request, self.template_name, context)
		except Usuario.DoesNotExist:
			return redirect('listado_usuarios')
		
class CambiarEstadoUsuario(ValidarUsuario, SingleObjectMixin, View):
	model = Usuario
	permission_required = 'anuncios.requiere_admin'

	def get(self, request, pk, *args, **kwargs):
		mensaje = ''
		self.object = Usuario.objects.filter(pk=pk).first()
		if self.object is None:
			return redirect('listado_usuarios')
		try:
			usuario = User.objects.get(username=self.object.cedula)
			if usuario.is_active:
				usuario.is_active = False
				mensaje = 'El usuario ha sido deshabilitado correctamente'
			elif not usuario.is_active:
				usuario.is_active = True
				mensaje = 'El usuario ha sido habilitado correctamente'
			usuario.save(update_fields=('is_active',))
			messages.success(request, mensaje)
			return redirect(request.META.get('HTTP_REFERER'))
		except User.DoesNotExist:
			return redirect('listado_usuarios')

class AccessoDenegadoView(TemplateView):
	template_name = 'registration/acceso_denegado.html'