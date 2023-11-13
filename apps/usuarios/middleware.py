from django.http import HttpResponseNotFound
from django.template.loader import get_template

class TemplateErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            template = get_template('base/404.html')
            response = HttpResponseNotFound(template.render())
        return response