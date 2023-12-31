from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from xhtml2pdf import pisa
import datetime
from django.http import JsonResponse
from django.shortcuts import redirect

from ...utils import link_callback
from apps.anuncios.models import Usuario
from django.contrib.auth.models import User
from apps.usuarios.mixins import ValidarUsuario

class ReporteUsuarios(ValidarUsuario, View):
	permission_required = 'anuncios.requiere_secretria'

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)
	
	def get(self, request, *args, **kwargs):
		try:
			formato_fecha = datetime.datetime.now().strftime("%d/%m/%Y")
			datos = Usuario.objects.filter(user__is_superuser=False).order_by('-id')
			context = {
				'report_title': 'Reporte de usuarios',
				'logo_img': '{}'.format('static/img/uce_logo.png'),
				'user': f'{request.user.get_full_name()}',
				'date': formato_fecha,
				'request':request,
				'datos': datos
			}
			template_path= get_template('reportes/reporte_usuarios.html')
			html = template_path.render(context)
			response = HttpResponse(content_type='application/pdf')
			pisa.CreatePDF(html, dest=response, link_callback=link_callback)
			return response
		
		except Exception as e:
			return JsonResponse({'error': str(e)}, safe=False)

class ReporteDetalleUsuario(ValidarUsuario, View):
	permission_required = 'anuncios.requiere_secretria'

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)
	
	def get(self, request, pk, *args, **kwargs):
		try:
			formato_fecha = datetime.datetime.now().strftime("%d/%m/%Y")
			anuncios = Usuario.objects.get(pk=pk)
			context = {
				'report_title': 'Reporte de detalle de usuario',
				'logo_img': '{}'.format('static/img/uce_logo.png'),
				'user': f'{request.user.get_full_name()}',
				'date': formato_fecha,
				'request':request,
				'datos': anuncios
			}
			template_path= get_template('reportes/reporte_detalle_usuario.html')
			html = template_path.render(context)
			response = HttpResponse(content_type='application/pdf')
			pisa.CreatePDF(html, dest=response, link_callback=link_callback)
			return response
		except Usuario.DoesNotExist:
			return redirect('listado_usuarios')
		except Exception as e:
			return JsonResponse({'error': str(e)}, safe=False)