from django import forms
from .models import Anuncios

class AnunciosForm(forms.ModelForm):
	class Meta:
		model = Anuncios
		fields = '__all__'