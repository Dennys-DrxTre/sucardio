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

class ListadoServicio(ListView):
	context_object_name = 'servicio_list'
	template_name = 'pages/servicios/listado_servicios.html'
	ordering = ['nombre_serv']
	model = Servicio
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Servicios"
		context["sub_title"] = "Listado de servicios"
		return context
	
class RegistrarServicio(SuccessMessageMixin, CreateView):
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