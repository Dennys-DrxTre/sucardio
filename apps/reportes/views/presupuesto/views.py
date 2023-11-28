from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from xhtml2pdf import pisa
import datetime
from django.http import JsonResponse
from django.shortcuts import redirect
from django.db.models import Q

from ...utils import link_callback
from apps.presupuestos.models import Presupuesto
from apps.anuncios.models import Usuario
from apps.usuarios.mixins import ValidarUsuario

class ReportePresupuestos(ValidarUsuario, View):
	permission_required = 'anuncios.requiere_secretria'

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

class ReporteDinamicoPresupuesto(ValidarUsuario, View):
	permission_required = 'anuncios.requiere_secretria'

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)
	
	def get(self, request, *args, **kwargs):
		try:
			date1 = request.GET.get('date1', '')
			date2 = request.GET.get('date2', '')
			search = request.GET.get('search', '')

			presupuestos = Presupuesto.objects.filter(fecha__range=(date1, date2))
			if search:
				presupuestos = presupuestos.filter(
					Q(metodo_pago__icontains=search) |
					Q(cliente__cedula__icontains=search)
				)
			presupuestos = presupuestos.order_by('-id')
			formato_fecha = datetime.datetime.now().strftime("%d/%m/%Y")

			# Convertir la cadena a un objeto datetime
			date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
			date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

			# Formatear el objeto datetime al formato deseado
			date1 = date1.strftime("%d/%m/%Y")
			date2 = date2.strftime("%d/%m/%Y")
			context = {
				'report_title': 'Listado de presupuestos',
				'logo_img': '{}'.format('static/img/uce_logo.png'),
				'user': f'{request.user.get_full_name()}',
				'presupuestos': presupuestos,
				'date': formato_fecha,
				'date1':date1,
				'date2':date2,
				'search': search,
				'request':request,
			}
			template_path= get_template('reportes/reporte_dinamico_presupuestos.html')
			html = template_path.render(context)
			response = HttpResponse(content_type='application/pdf')
			pisa.CreatePDF(html, dest=response, link_callback=link_callback)
			return response
		except Presupuesto.DoesNotExist:
			return redirect('listado_presupuestos')
		except Exception as e:
			return JsonResponse({'error': str(e)}, safe=False)

class ReporteDetallePresupuesto(ValidarUsuario, View):
	permission_required = 'anuncios.requiere_secretria'

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
		
class ReporteDetalleMiPresupuesto(ValidarUsuario, View):
	permission_required = 'anuncios.requiere_usuario'
	
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