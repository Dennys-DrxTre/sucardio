from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from ...forms import MedicoForm, MedicoEditForm
from django.views.generic import (
	UpdateView,
	ListView,
	CreateView,
	DetailView
)
from ...models import Medico
from django.contrib.auth.models import User


class ListadoMedico( ListView):
	context_object_name = 'medico_list'
	template_name = 'pages/medico/listado_medico.html'
	ordering = ['nombre']

	def get_queryset(self):
		return Medico.objects.all()
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Medicos"
		context["sub_title"] = "Listado de medicos"
		return context

class RegistrarMedico(SuccessMessageMixin, CreateView):
	template_name = 'pages/medico/registrar_medico.html'
	model = Medico
	form_class = MedicoForm
	success_url = '/listado-de-medicos/'
	success_message = "Medico creado exitosamente"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Medico"
		context["sub_title"] = "Registrar medico"
		return context

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