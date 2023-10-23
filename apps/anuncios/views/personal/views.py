from django.views.generic import (
    TemplateView,
    ListView
)
from ...models import Usuario


class ListadoPersonal(ListView):
    context_object_name = 'personal_list'
    template_name = 'pages/personal/listado_personal.html'
    ordering = ['nombre']

    def get_queryset(self):
        return Usuario.objects.exclude(tipo_usuario=Usuario.Permission.CLIENTE)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Personal"
        context["sub_title"] = "Listado de personal"
        return context