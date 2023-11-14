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
from apps.presupuestos.models import Presupuesto
from apps.anuncios.models import Usuario

class ReportePresupuestos(View):

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)
	
	def get(self, request, *args, **kwargs):
		try:
			formato_fecha = datetime.datetime.now().strftime("%d/%m/%Y")
			datos = Presupuesto.objects.all().order_by('-id')
			context = {
				'report_title': 'Reporte de presupuestos',
				'logo_img': '{}'.format('static/img/uce_logo.png'),
				'user': f'{request.user.get_full_name()}',
				'date': formato_fecha,
				'request':request,
				'datos': datos
			}
			template_path= get_template('reportes/reporte_presupuestos.html')
			html = template_path.render(context)
			response = HttpResponse(content_type='application/pdf')
			pisa.CreatePDF(html, dest=response, link_callback=link_callback)
			return response
		
		except Exception as e:
			return JsonResponse({'error': str(e)}, safe=False)

class ReporteDetallePresupuesto(View):

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)
	
	def get(self, request, pk, *args, **kwargs):
		try:
			formato_fecha = datetime.datetime.now().strftime("%d/%m/%Y")
			datos = Presupuesto.objects.get(pk=pk)
			context = {
				'report_title': 'Reporte de detalle de presupuesto',
				'logo_img': '{}'.format('static/img/uce_logo.png'),
				'user': f'{request.user.get_full_name()}',
				'date': formato_fecha,
				'request':request,
				'datos': datos
			}
			template_path= get_template('reportes/reporte_detalle_presupuesto.html')
			html = template_path.render(context)
			response = HttpResponse(content_type='application/pdf')
			pisa.CreatePDF(html, dest=response, link_callback=link_callback)
			return response
		except Presupuesto.DoesNotExist:
			return redirect('listado_presupuestos')
		except Exception as e:
			return JsonResponse({'error': str(e)}, safe=False)
		
class ReporteDetalleMiPresupuesto(View):

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)
	
	def get(self, request, pk, *args, **kwargs):
		try:
			formato_fecha = datetime.datetime.now().strftime("%d/%m/%Y")
			usuario = Usuario.objects.filter(user = request.user.pk).first()
			datos = Presupuesto.objects.get(pk=pk, cliente__cedula=usuario.cedula)
			context = {
				'report_title': 'Reporte de detalle de presupuesto',
				'logo_img': '{}'.format('static/img/uce_logo.png'),
				'user': f'{request.user.get_full_name()}',
				'date': formato_fecha,
				'request':request,
				'datos': datos
			}
			template_path= get_template('reportes/reporte_detalle_presupuesto.html')
			html = template_path.render(context)
			response = HttpResponse(content_type='application/pdf')
			pisa.CreatePDF(html, dest=response, link_callback=link_callback)
			return response
		except Presupuesto.DoesNotExist:
			return redirect('mi_presupuesto')
		except Exception as e:
			return JsonResponse({'error': str(e)}, safe=False)