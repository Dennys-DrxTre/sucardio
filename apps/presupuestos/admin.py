from django.contrib import admin
from apps.presupuestos.models import Servicio, Presupuesto, DetallePresupuesto

# Register your models here.
admin.site.register(Servicio)
admin.site.register(Presupuesto)
admin.site.register(DetallePresupuesto)
