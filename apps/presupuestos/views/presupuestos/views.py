from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from ...forms import PresupuestoForm
from django.views.generic import (
	UpdateView,
	ListView,
	TemplateView,
	DetailView,
	View
)
from django.views.generic.detail import SingleObjectMixin
from ...models import Presupuesto

class ListadoPresupuesto(LoginRequiredMixin, ListView):
	context_object_name = 'presupuesto_list'
	template_name = 'pages/presupuestos/listado_presupuesto.html'
	ordering = ['-id']
	model = Presupuesto

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Presupuestos"
		context["sub_title"] = "Listado de presupuestos"
		return context

class RegistrarPresupuesto(LoginRequiredMixin, TemplateView):
	template_name = 'pages/presupuestos/registrar_presupuesto.html'
	object = None

	def get_success_url(self):
		return reverse('detalle_presupuesto', kwargs={'pk': self.object.pk})

	def post(self, request, *args, **kwargs):
		form = PresupuestoForm(request.POST)
		if form.is_valid():
			presupuesto = Presupuesto()
			presupuesto.cliente = form.cleaned_data['cliente']
			presupuesto.metodo_pago = form.cleaned_data['metodo_pago']
			presupuesto.save()
			for s in form.cleaned_data['servicio']:
				presupuesto.servicio.add(s.pk)
				presupuesto.total += s.precio_serv
			presupuesto.save()
			self.object = presupuesto
			messages.success(request, 'El presupuesto se ha registrado correctamente')
			return redirect(self.get_success_url())
		else:
			context = self.get_context_data(**kwargs)
			context["form"] = form
			return render(request, self.template_name, context)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Presupuestos"
		context["sub_title"] = "Registrar presupuesto"
		context["form"] = PresupuestoForm
		return context

class EditarPresupuesto(LoginRequiredMixin, UpdateView):
	template_name = 'pages/presupuestos/registrar_presupuesto.html'
	object = None

	def get_success_url(self):
		return reverse('detalle_presupuesto', kwargs={'pk': self.object.pk})

	def get(self, request, *args, **kwargs):
		context = {}
		self.object = Presupuesto.objects.get(pk=kwargs['pk'])
		form = PresupuestoForm(instance=self.object)
		context["title"] = "Presupuestos"
		context["sub_title"] = "Editar presupuesto"
		context["form"] = form
		return render(request, self.template_name, context)
	
	def post(self, request, *args, **kwargs):
		self.object = Presupuesto.objects.filter(pk=kwargs['pk']).first()
		total = 0.00
		form = PresupuestoForm(request.POST, instance=self.object)
		if form.is_valid():
			self.object = form.save(commit=False)
			for s in form.cleaned_data['servicio']:
				self.object.servicio.add(s.pk)
				total += s.precio_serv
				self.object.total = total
			self.object.save()
			messages.success(request, 'El presupuesto se ha editado correctamente')
			return redirect(self.get_success_url())
		else:
			context = self.get_context_data(**kwargs)
			self.object = Presupuesto.objects.get(pk=kwargs['pk'])
			form = PresupuestoForm(instance=self.object)
			return render(request, self.template_name, context)
	
class DetallePresupuesto(LoginRequiredMixin, DetailView):
	template_name = 'pages/presupuestos/detalle_presupuesto.html'
	model = Presupuesto
	context_object_name = 'presupuesto'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Presupuestos"
		context["sub_title"] = "Detalle del presupuesto"
		return context