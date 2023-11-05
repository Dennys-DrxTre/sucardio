from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
	class Meta:
		model = Servicio
		fields = '__all__'

	def clean_cedula(self):
		data = self.cleaned_data['nombre_serv']
		if Servicio.objects.filter(nombre_serv=data).exists():
			raise forms.ValidationError('El Servicio ya existe.')
		return data
	
class ServicioEditForm(forms.ModelForm):
	class Meta:
		model = Servicio
		fields = '__all__'

	def clean_cedula(self):
		data = self.cleaned_data['nombre_serv']
		qs = Servicio.objects.exclude(id=self.instance.id).filter(nombre_serv=data)
		if qs.exists():
			raise forms.ValidationError('El Servicio ya existe.')
		return data