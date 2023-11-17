from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.db.models import Q
from xhtml2pdf import pisa
import datetime
from datetime import date
from django.http import JsonResponse
from django.shortcuts import redirect

from ...utils import link_callback
from apps.citas.models import Cita, Medico, Usuario

class ReportePrueba(View):

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)
	
	def get(self, request, *args, **kwargs):
		try:
			formato_fecha = datetime.datetime.now().strftime("%d/%m/%Y")
			context = {
				'report_title': 'Reporte de prueba',
				'logo_img': '{}'.format('static/img/uce_logo.png'),
				'user': f'{request.user.get_full_name()}',
				'date': formato_fecha,
				'request':request,
			}
			template_path= get_template('reportes/prueba.html')
			html = template_path.render(context)
			response = HttpResponse(content_type='application/pdf')
			pisa.CreatePDF(html, dest=response, link_callback=link_callback)
			return response
		
		except Exception as e:
			return JsonResponse({'error': str(e)}, safe=False)

class DetalleCita(View):

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)
	
	def get(self, request, pk, *args, **kwargs):
		try:
			cita = Cita.objects.get(pk = pk)
			formato_fecha = datetime.datetime.now().strftime("%d/%m/%Y")
			context = {
				'report_title': 'Detalle de cita',
				'logo_img': '{}'.format('static/img/uce_logo.png'),
				'user': f'{request.user.get_full_name()}',
				'cita': cita,
				'date': formato_fecha,
				'request':request,
			}
			template_path= get_template('reportes/det_cita.html')
			html = template_path.render(context)
			response = HttpResponse(content_type='application/pdf')
			pisa.CreatePDF(html, dest=response, link_callback=link_callback)
			return response
		except Cita.DoesNotExist:
			return redirect('listado_citas')
		except Exception as e:
			return JsonResponse({'error': str(e)}, safe=False)
		
class DetalleMiCita(View):

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)
	
	def get(self, request, pk, *args, **kwargs):
		try:
			usuario = Usuario.objects.get(user__username=request.user.username)
			cita = Cita.objects.get(pk = pk, cliente__cedula=usuario.cedula)
			if cita.estado != 'PE':
				formato_fecha = datetime.datetime.now().strftime("%d/%m/%Y")
				context = {
					'report_title': 'Detalle de cita',
					'logo_img': '{}'.format('static/img/uce_logo.png'),
					'user': f'{request.user.get_full_name()}',
					'cita': cita,
					'date': formato_fecha,
					'request':request,
				}
				template_path= get_template('reportes/det_cita.html')
				html = template_path.render(context)
				response = HttpResponse(content_type='application/pdf')
				pisa.CreatePDF(html, dest=response, link_callback=link_callback)
				return response
			else:
				return redirect('mis_citas')
		except Cita.DoesNotExist:
			return redirect('mis_citas')
		except Usuario.DoesNotExist:
			return redirect('mis_citas')
		except Exception as e:
			return JsonResponse({'error': str(e)}, safe=False)

class CitasDelDia(View):

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)
	
	def get(self, request, pk,*args, **kwargs):
		try:
			formato_fecha = datetime.datetime.now().strftime("%d/%m/%Y")
			fecha_actual = date.today()
			cita = Cita.objects.filter(medico__cedula = pk, fecha_cita = fecha_actual, estado = 'AP' )
			medico = Medico.objects.get(cedula = pk)
			context = {
				'report_title': 'Citas aprobadas para el dia',
				'logo_img': '{}'.format('static/img/uce_logo.png'),
				'user': f'{request.user.get_full_name()}',
				'cita': cita,
				'medico': medico,
				'date': formato_fecha,
				'request':request,
			}
			template_path= get_template('reportes/citas_dia.html')
			html = template_path.render(context)
			response = HttpResponse(content_type='application/pdf')
			pisa.CreatePDF(html, dest=response, link_callback=link_callback)
			return response
		
		except Exception as e:
			return JsonResponse({'error': str(e)}, safe=False)