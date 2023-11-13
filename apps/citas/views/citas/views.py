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
	DetailView, 
	TemplateView
)
from ...models import Cita, Usuario, Medico
from ...forms import CitasForm


class ListadoCita(ListView):
	context_object_name = 'cita_list'
	template_name = 'pages/citas/listado_citas.html'
	ordering = ['-id']

	def get_queryset(self):
		return Cita.objects.all()
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Citas"
		context["sub_title"] = "Listado de citas"
		context['medicos'] = Medico.objects.all()
		return context

"""
class DetallesCita(SuccessMessageMixin, DetailView):
	template_name = 'pages/citas/detalles_cita.html'
	model = Cita
	context_object_name = 'cita'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Cita"
		context["sub_title"] = "Detalle de cita"
		return context
"""

class DetallesCita(LoginRequiredMixin, TemplateView):
	template_name = 'pages/citas/detalles_cita.html'

	def get(self, request, pk,*args, **kwargs):
		context = {}

		usuario = Usuario.objects.filter(user = request.user.pk).first()
		citas = Cita.objects.filter(pk=pk, cliente__cedula=usuario.cedula).first()
		if citas:
			context['cita'] = citas
			context["sub_title"] = "Detalle de mi cita"
			return render(request, self.template_name, context)
		else:
			return redirect('mis_citas')

class EditarCita(SuccessMessageMixin, UpdateView):
	template_name = 'pages/citas/editar_cita.html'
	model = Cita
	fields = ['fecha_cita', 'estado']
	success_url = '/listado-de-citas/'
	success_message = "Cita editada exitosamente"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Cita"
		context["sub_title"] = "Editar cita"
		return context
