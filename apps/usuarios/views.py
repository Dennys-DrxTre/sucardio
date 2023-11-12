from itertools import chain

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from apps.citas.models import Medico, Cita
from apps.presupuestos.models import Presupuesto
from apps.anuncios.models import Anuncios, Usuario
from django.contrib.auth.models import User

from .forms import LoginForm, SearchForm, ChangePass

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
				return redirect('/inicio/') # redirige al usuario a la página de inicio después de iniciar sesión
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

class ChangePassword(LoginRequiredMixin, TemplateView):
	template_name = 'registration/cambiar_clave.html'

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


class SearchView(LoginRequiredMixin, View):
	template_name = 'base/search.html'
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

class ListadoUsuarios(LoginRequiredMixin, TemplateView):
	template_name = 'pages/usuarios/listado_usuarios.html'

	def get(self, request, *args, **kwargs):
		context = {}
		context['sub_title'] = 'Listado de usuarios'
		context['title'] = 'Usuarios'

		usuarios = Usuario.objects.filter(user__is_active=True).order_by('cedula')

		paginator = Paginator(usuarios, 10)  # Muestra 10 resultados por página

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

		return render(request, self.template_name, context)