from django import forms
from apps.anuncios.models import Usuario
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

class ChangePass(forms.Form):
    pass_actual = forms.CharField(max_length=63, widget=forms.PasswordInput)
    nueva_pas1 = forms.CharField(max_length=63, widget=forms.PasswordInput)
    nueva_pas2 = forms.CharField(max_length=63, widget=forms.PasswordInput)

class SearchForm(forms.Form):
    search = forms.CharField()

class RegistrarUsuarioAdmin(forms.ModelForm):
   password = forms.CharField(max_length=63, widget=forms.PasswordInput)
   password2 = forms.CharField(max_length=63, widget=forms.PasswordInput)

   class Meta:
      model = Usuario
      fields = '__all__'

   def clean(self):
      cleaned_data = super().clean()
      cedula = cleaned_data.get("cedula")
      password = cleaned_data.get("password")
      password2 = cleaned_data.get("password2")

      # Verificar si el usuario ya existe
      if User.objects.filter(username=cedula).exists():
         self.add_error('cedula', 'Un usuario con esta cedula de usuario ya existe.')

      # Verificar si las contraseñas son iguales
      if password != password2:
         self.add_error('password', 'Las contraseñas no coinciden.')

class EditarUsuarioAdmin(forms.ModelForm):

   class Meta:
      model = Usuario
      fields = '__all__'
      exclude = ['user','fecha_registro']

   def clean(self):
      cleaned_data = super().clean()
      cedula = cleaned_data.get("cedula")

      # Verificar si el usuario ya existe
      if Usuario.objects.exclude(pk=self.instance.pk).filter(cedula=cedula).exists():
         self.add_error('cedula', 'Un usuario con esta cedula de usuario ya existe.')

class EditarPasswordUsuarioForm(forms.ModelForm):
   password = forms.CharField(max_length=63, widget=forms.PasswordInput)
   password2 = forms.CharField(max_length=63, widget=forms.PasswordInput)

   class Meta:
      model = Usuario
      fields = ['cedula','nombre']

   def clean(self):
      cleaned_data = super().clean()
      password = cleaned_data.get("password")
      password2 = cleaned_data.get("password2")

      # Verificar si las contraseñas son iguales
      if password != password2:
         self.add_error('password', 'Las contraseñas no coinciden.')