from django.contrib import admin
from apps.presupuestos.models import Servicio, Presupuesto

# Register your models here.
admin.site.register(Servicio)
admin.site.register(Presupuesto)
