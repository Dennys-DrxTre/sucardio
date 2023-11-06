from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import (
	UpdateView,
	ListView,
	CreateView,
	DetailView,
	View
)
from .models import Anuncios
from .forms import AnunciosForm

class ListadoAnuncioAdmin(LoginRequiredMixin, ListView):
	context_object_name = 'anuncio_list'
	template_name = 'pages/anuncios/lista_de_anuncios.html'
	model= Anuncios
	ordering = ['-id']
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Anuncios"
		context["sub_title"] = "Listado de anuncios"
		return context

class ListadoAnuncios( ListView):
	context_object_name = 'anuncio_list'
	template_name = 'landingpage/pages/listado_de_anuncios.html'
	model= Anuncios
	
	def get_queryset(self):
		return Anuncios.objects.filter(estado='AC').order_by('-id')
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Anuncios"
		context["sub_title"] = "Listado de anuncios"
		return context

class RegistrarAnuncio(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = 'pages/anuncios/crear_anuncio.html'
	model = Anuncios
	form_class = AnunciosForm
	success_url = '/listado-de-anuncios/'
	success_message = "El anuncio se ha creado exitosamente."

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Anuncios"
		context["sub_title"] = "Registrar anuncio"
		return context

class EditarAnuncio(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	template_name = 'pages/anuncios/editar_anuncio.html'
	model = Anuncios
	form_class = AnunciosForm
	success_url = '/listado-de-anuncios/'
	success_message = "El anuncio se ha editado exitosamente."

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Anuncios"
		context["sub_title"] = "Editar anuncio"
		return context

class DetalleAnuncio(LoginRequiredMixin, DetailView):
	template_name = 'pages/anuncios/detalle_anuncio.html'
	model = Anuncios
	context_object_name = 'anuncio'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Anuncios"
		context["sub_title"] = "Detalles del anuncio"
		return context

class DetalleAnuncioLanding(DetailView):
	template_name = 'landingpage/pages/detalle_anuncio.html'
	model = Anuncios
	context_object_name = 'anuncio'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Anuncios"
		context["sub_title"] = "Detalles del anuncio"
		return context

class CambiarEstadoAnuncio(LoginRequiredMixin, SingleObjectMixin, View):
	model = Anuncios

	def get(self, request, *args, **kwargs):
		mensaje = ''
		self.object = self.get_object()
		if self.object.estado == 'AC':
			self.object.estado = 'DE'
			mensaje = 'El anuncio ha sido deshabilitado correctamente'
		elif self.object.estado == 'DE':
			self.object.estado = 'AC'
			mensaje = 'El anuncio ha sido habilitado correctamente'
		self.object.save(update_fields=('estado',))
		messages.success(request, mensaje)

		return redirect(request.META.get('HTTP_REFERER'))