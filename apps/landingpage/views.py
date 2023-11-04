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
    template_name = 'landingpage/pages/registrar_cita.html'

class DetalleMiCita(TemplateView):
    template_name = 'landingpage/pages/registrar_cita.html'