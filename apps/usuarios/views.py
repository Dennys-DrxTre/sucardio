from itertools import chain

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.citas.models import Medico, Usuario, Cita
from apps.presupuestos.models import Presupuesto
from apps.anuncios.models import Anuncios

from .forms import LoginForm, SearchForm

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
			context['results'] = results
			context['total_results'] = total_results
			context['query'] = query
		else:
			results = []
		return render(request, self.template_name, context)