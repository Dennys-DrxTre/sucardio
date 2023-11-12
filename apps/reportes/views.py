from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from xhtml2pdf import pisa
import datetime
from django.http import JsonResponse

from .utils import link_callback

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