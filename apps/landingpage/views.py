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
from apps.citas.models import Cita, Usuario
from apps.presupuestos.models import Presupuesto
from apps.citas.forms import CitasForm

class Inicio(TemplateView):
	template_name = 'landingpage/pages/inicio.html'
	
class MisCitas(ListView):
	template_name = 'landingpage/pages/mis_citas.html'
	model = Cita
	context_object_name = 'cita_list'

	def get_queryset(self):
		return Cita.objects.filter(cliente=self.request.user.pk).order_by('-id')

class RegistrarCita(SuccessMessageMixin, TemplateView):
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

class ListadoPresupuesto(TemplateView):
	context_object_name = 'presupuesto_list'
	template_name = 'landingpage/pages/presupuesto/mi_presupuesto.html'
	ordering = ['-id']

	def get(self, request, *args, **kwargs):
		mi_presupuesto = Presupuesto.objects.filter(cliente=request.user.pk)
		context = {}
		context["title"] = "Presupuestos"
		context["sub_title"] = "Listado de presupuestos"
		context['presupuestos'] = mi_presupuesto
		return render(request, self.template_name, context)

class DetalleMiCita(TemplateView):
	template_name = 'landingpage/pages/detalle_de_mi_cita.html'

class Anuncios(TemplateView):
	template_name = 'landingpage/pages/listado_de_anuncios.html'

class Contacto(TemplateView):
	template_name = 'landingpage/pages/contacto.html'

class SobreNosotros(TemplateView):
	template_name = 'landingpage/pages/sobre_nosotros.html'