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

class Inicio(TemplateView):
    template_name = 'landingpage/pages/inicio.html'
    
class MisCitas(TemplateView):
    template_name = 'landingpage/pages/mis_citas.html'

class SolicitarCita(TemplateView):
    template_name = 'landingpage/pages/solicitar_cita.html'

class DetalleMiCita(TemplateView):
    template_name = 'landingpage/pages/detalle_de_mi_cita.html'

class Anuncios(TemplateView):
    template_name = 'landingpage/pages/listado_de_anuncios.html'

class Contacto(TemplateView):
    template_name = 'landingpage/pages/contacto.html'