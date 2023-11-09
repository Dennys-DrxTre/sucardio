from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.views.generic import (
	UpdateView,
	ListView,
	CreateView,
	DetailView,
	View,
	TemplateView
)
from apps.citas.models import Cita, Usuario
from apps.citas.forms import CitasForm
from apps.presupuestos.models import Presupuesto
from apps.presupuestos.forms import MiPresupuestoForm

class Inicio(TemplateView):
	template_name = 'landingpage/pages/inicio.html'
	
class MisCitas(LoginRequiredMixin, TemplateView):
	template_name = 'landingpage/pages/mis_citas.html'

	def get(self, request, *args, **kwargs):
		context = {}
		citas = Cita.objects.filter(cliente=self.request.user.pk).order_by('-id')
		paginator = Paginator(citas, 8)  # Muestra 10 resultados por página

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

		context["sub_title"] = "Mis citas"
		context["cita_list"] = page_obj
		return render(request, self.template_name, context)

class RegistrarCita(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
	template_name = 'landingpage/pages/solicitar_cita.html'
	success_url = '/mis-citas/'
	success_message = "Solicitud para cita creada exitosamente, se le estará notificando el estado de la misma"

	def post(self, request, *args, **kwargs):
		form = CitasForm(request.POST)
		if form.is_valid():
			cliente = Usuario.objects.filter(user=request.user.pk).first()
			cita = Cita()
			cita.cliente = cliente
			cita.control_pac = form.cleaned_data['control_pac']
			cita.motivo_consulta = form.cleaned_data['motivo_consulta']
			cita.metodo_pago = form.cleaned_data['metodo_pago']
			cita.medico = form.cleaned_data['medico']
			cita.save()

			messages.success(request, self.success_message)
			return redirect(self.success_url)
		else:
			context = self.get_context_data(**kwargs)
			context["form"] = form
			return render(request, self.template_name, context)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Citas"
		context["sub_title"] = "Solititar cita"
		context['form'] = CitasForm()
		return context  

class ListadoMiPresupuesto(LoginRequiredMixin, TemplateView):
	context_object_name = 'presupuesto_list'
	template_name = 'landingpage/pages/presupuesto/mi_presupuesto.html'

	def get(self, request, *args, **kwargs):
		mi_presupuesto = Presupuesto.objects.filter(cliente=request.user.pk).order_by('-id')

		paginator = Paginator(mi_presupuesto, 8)  # Muestra 10 resultados por página

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

		context = {}
		context["title"] = "Presupuestos"
		context["sub_title"] = "Mis presupuestos"
		context['presupuestos'] = page_obj
		return render(request, self.template_name, context)

class RegistrarMiPresupuesto(LoginRequiredMixin, TemplateView):
	template_name = 'landingpage/pages/presupuesto/registrar_mi_presupuesto.html'
	object = None

	def get_success_url(self):
		return reverse('detalle_mi_presupuesto', kwargs={'pk': self.object.pk})

	def post(self, request, *args, **kwargs):
		form = MiPresupuestoForm(request.POST)
		usuario = Usuario.objects.filter(user=request.user.pk).first()
		if form.is_valid():
			presupuesto = Presupuesto()
			presupuesto.cliente = usuario
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
		context["sub_title"] = "Registrar mi presupuesto"
		context["form"] = MiPresupuestoForm()
		return context

class DetalleMiPresupuesto(LoginRequiredMixin, TemplateView):
	template_name = 'landingpage/pages/presupuesto/detalle_mi_presupuesto.html'

	def get(self, request, pk,*args, **kwargs):
		context = {}

		usuario = Usuario.objects.filter(user = request.user.pk).first()
		presupuesto = Presupuesto.objects.filter(pk=pk, cliente__cedula=usuario.cedula).first()
		if presupuesto:
			context['presupuesto'] = presupuesto
			context["sub_title"] = "Detalle de mi presupuesto"
			return render(request, self.template_name, context)
		else:
			return redirect('mi_presupuesto')

class DetalleMiCita(LoginRequiredMixin, DetailView):
	template_name = 'landingpage/pages/detalle_de_mi_cita.html'
	model = Cita
	context_object_name = 'cita'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Citas"
		context["sub_title"] = "Detalle de cita"
		return context


class Contacto(TemplateView):
	template_name = 'landingpage/pages/contacto.html'

class SobreNosotros(TemplateView):
	template_name = 'landingpage/pages/sobre_nosotros.html'