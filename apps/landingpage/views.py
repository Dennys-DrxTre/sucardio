from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import (
	UpdateView,
	ListView,
	CreateView,
	DetailView,
	View,
	TemplateView
)
from apps.citas.models import Cita
from apps.citas.forms import CitasForm

class Inicio(TemplateView):
	template_name = 'landingpage/pages/inicio.html'
	
class MisCitas(ListView):
	template_name = 'landingpage/pages/mis_citas.html'
	model = Cita
	context_object_name = 'cita_list'

	def get_queryset(self):
		return Cita.objects.filter(cliente=self.request.user.pk).order_by('-id')

class RegistrarCita(SuccessMessageMixin, CreateView):
	template_name = 'landingpage/pages/solicitar_cita.html'
	model = Cita
	form_class = CitasForm
	success_url = '/mis-citas/'
	success_message = "Solicitud para cita creada exitosamente, se le estará notificando el estado de la misma"

	# def form_valid(self, form):
	# 	form.instance.cliente_id = self.request.user.pk
	# 	messages.success(self.request, self.success_message)
	# 	return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Citas"
		context["sub_title"] = "Registrar citas"
		return context  

class DetalleMiCita(TemplateView):
	template_name = 'landingpage/pages/detalle_de_mi_cita.html'

class Anuncios(TemplateView):
	template_name = 'landingpage/pages/listado_de_anuncios.html'

class Contacto(TemplateView):
	template_name = 'landingpage/pages/contacto.html'

class SobreNosotros(TemplateView):
	template_name = 'landingpage/pages/sobre_nosotros.html'