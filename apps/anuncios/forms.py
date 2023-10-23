from django import forms
from .models import Usuario
from django.core.exceptions import ValidationError

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
