from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from ...forms import PresupuestoForm
from django.views.generic import (
	UpdateView,
	ListView,
	TemplateView,
	DetailView,
	View
)
from django.views.generic.detail import SingleObjectMixin
from ...models import Presupuesto, Servicio

class ListadoPresupuesto(ListView):
	context_object_name = 'presupuesto_list'
	template_name = 'pages/presupuestos/listado_presupuesto.html'
	ordering = ['-id']
	model = Presupuesto

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Presupuestos"
		context["sub_title"] = "Listado de presupuestos"
		return context

class RegistrarPresupuesto(TemplateView):
	template_name = 'pages/presupuestos/registrar_presupuesto.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Presupuestos"
		context["sub_title"] = "Registrar presupuesto"
		context["form"] = PresupuestoForm
		return context