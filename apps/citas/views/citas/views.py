from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.views.generic import (
	UpdateView,
	ListView,
	CreateView,
	DetailView
)
from ...models import Cita
from ...forms import CitasForm



class ListadoCita( ListView):
	context_object_name = 'cita_list'
	template_name = 'pages/citas/listado_citas.html'
	ordering = ['-id']

	def get_queryset(self):
		return Cita.objects.all()
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Citas"
		context["sub_title"] = "Listado de citas"
		return context

class RegistrarCita(SuccessMessageMixin, CreateView):
	template_name = 'pages/citas/registrar_cita.html'
	model = Cita
	form_class = CitasForm
	success_url = '/listado-de-citas/'
	success_message = "Solicitud para cita creada exitosamente, se le estará notificando el estado de la misma"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Citas"
		context["sub_title"] = "Registrar citas"
		return context
"""
class EditarMedico(SuccessMessageMixin, UpdateView):
	template_name = 'pages/medico/registrar_medico.html'
	model = Medico
	form_class = MedicoEditForm
	success_url = '/listado-de-medicos/'
	success_message = "Medico editado exitosamente"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Medico"
		context["sub_title"] = "Editar medico"
		return context

class DetalleMedico(SuccessMessageMixin, DetailView):
	template_name = 'pages/medico/detalle_medico.html'
	model = Medico
	context_object_name = 'medico'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Medico"
		context["sub_title"] = "Detalle del medico"
		return context
"""