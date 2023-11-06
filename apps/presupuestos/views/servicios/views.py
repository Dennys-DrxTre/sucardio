from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from ...forms import ServicioForm, ServicioEditForm
from django.views.generic import (
	UpdateView,
	ListView,
	CreateView,
	DetailView,
	View
)
from django.views.generic.detail import SingleObjectMixin
from ...models import Servicio

class ListadoServicio(LoginRequiredMixin, ListView):
	context_object_name = 'servicio_list'
	template_name = 'pages/servicios/listado_servicios.html'
	ordering = ['nombre_serv']

	def get_queryset(self):
		estado = self.request.GET.get('estado', None)
		if estado:
			return Servicio.objects.filter(estado=estado)
		else:
			return Servicio.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		nombre_estado = {
			None:'Todos',
			'AC':'Habilitados',
			'DE':'Deshabilitados'
		}
		estado = self.request.GET.get('estado', None)
		context["title"] = "Servicios"
		context["sub_title"] = "Listado de servicios"
		context['nombre_estado'] = nombre_estado[estado]
		return context
	
class RegistrarServicio(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	template_name = 'pages/servicios/registrar_servicio.html'
	model = Servicio
	form_class = ServicioForm
	success_url = '/listado-de-servicios/'
	success_message = "Servicio creado exitosamente"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Servicios"
		context["sub_title"] = "Registrar servicio"
		return context
	
class EditarServicio(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
	template_name = 'pages/servicios/registrar_servicio.html'
	model = Servicio
	form_class = ServicioEditForm
	success_url = '/listado-de-servicios/'
	success_message = "Servicio editado exitosamente"
		
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Servicios"
		context["sub_title"] = "Editar Servicio"
		return context
	
class DetalleServicio(LoginRequiredMixin, SuccessMessageMixin, DetailView):
	template_name = 'pages/servicios/detalle_servicio.html'
	model = Servicio
	context_object_name = 'servicio'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Servicios"
		context["sub_title"] = "Detalle del Servicio"
		return context

class CambiarEstadoServicio(LoginRequiredMixin, SingleObjectMixin, View):
	model = Servicio

	def get(self, request, *args, **kwargs):
		mensaje = ''
		self.object = self.get_object()
		if self.object.estado == 'AC':
			self.object.estado = 'DE'
			mensaje = 'El servicio ha sido deshabilitado correctamente'
		elif self.object.estado == 'DE':
			self.object.estado = 'AC'
			mensaje = 'El servicio ha sido habilitado correctamente'
		self.object.save(update_fields=('estado',))
		messages.success(request, mensaje)

		return redirect(request.META.get('HTTP_REFERER'))