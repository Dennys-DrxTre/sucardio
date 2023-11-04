from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
	UpdateView,
	ListView,
	CreateView,
	DetailView
)
from .models import Anuncios
from .forms import AnunciosForm

class ListadoAnuncioAdmin(ListView):
	context_object_name = 'anuncio_list'
	template_name = 'pages/anuncios/lista_de_anuncios.html'
	model= Anuncios
	ordering = ['-id']
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Anuncios"
		context["sub_title"] = "Listado de anuncios"
		return context

class ListadoAnuncios( ListView):
	context_object_name = 'anuncio_list'
	template_name = 'landingpage/pages/listado_de_anuncios.html'
	model= Anuncios
	ordering = ['-id']
	
	def get_queryset(self):
		return Anuncios.objects.filter(estado='AC').order_by('-id')
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Anuncios"
		context["sub_title"] = "Listado de anuncios"
		return context

class RegistrarAnuncio(SuccessMessageMixin, CreateView):
	template_name = 'pages/anuncios/crear_anuncio.html'
	model = Anuncios
	form_class = AnunciosForm
	success_url = '/listado-de-anuncios/'
	success_message = "El anuncio se ha creado exitosamente."

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Anuncios"
		context["sub_title"] = "Registrar anuncio"
		return context