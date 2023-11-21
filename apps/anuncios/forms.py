from django import forms
from .models import Anuncios, Usuario

class AnunciosForm(forms.ModelForm):
	autor = forms.ModelChoiceField(queryset=Usuario.objects.exclude(tipo_usuario=Usuario.Permission.CLIENTE).filter(user__is_active=True,user__is_superuser=False))
	class Meta:
		model = Anuncios
		fields = '__all__'