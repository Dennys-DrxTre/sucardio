from django import forms
from .models import Servicio, Presupuesto
from apps.citas.models import Medico

class ServicioForm(forms.ModelForm):
	class Meta:
		model = Servicio
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(ServicioForm, self).__init__(*args, **kwargs)
		self.fields['medico'].queryset = Medico.objects.filter(estado='AC')

	def clean_nombre_serv(self):
		data = self.cleaned_data['nombre_serv']
		if Servicio.objects.filter(nombre_serv=data).exists():
			raise forms.ValidationError('El Servicio ya existe.')
		return data
	
class ServicioEditForm(forms.ModelForm):
	class Meta:
		model = Servicio
		fields = '__all__'

	def clean_nombre_serv(self):
		data = self.cleaned_data['nombre_serv']
		qs = Servicio.objects.exclude(id=self.instance.id).filter(nombre_serv=data)
		if qs.exists():
			raise forms.ValidationError('El Servicio ya existe.')
		return data
	
class PresupuestoForm(forms.ModelForm):
	class Meta:
		model = Presupuesto
		fields = '__all__'

class MiPresupuestoForm(forms.ModelForm):
	class Meta:
		model = Presupuesto
		exclude = ('cliente',)
