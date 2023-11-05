from django import forms
from apps.citas.models import Medico, Cita

class MedicoForm(forms.ModelForm):
	class Meta:
		model = Medico
		fields = '__all__'

	def clean_cedula(self):
		data = self.cleaned_data['cedula']
		if Medico.objects.filter(cedula=data).exists():
			raise forms.ValidationError('El Medico ya existe.')
		return data
	
class MedicoEditForm(forms.ModelForm):
	class Meta:
		model = Medico
		fields = '__all__'

	def clean_cedula(self):
		data = self.cleaned_data['cedula']
		qs = Medico.objects.exclude(id=self.instance.id).filter(cedula=data)
		if qs.exists():
			raise forms.ValidationError('El Medico ya existe.')
		return data

class CitasForm(forms.ModelForm):
	class Meta:
		model = Cita
		exclude = ('fecha_cita', 'estado',)

# class PersonalForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = '__all__'

# class UserForm(forms.ModelForm):
#     password1 = forms.CharField(label='Contrasena', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm Contrasena', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_active']

#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Las contrasena no coinciden")
#         return password2

#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError("El email ya está en uso.")
#         return email

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user

# class UserFormEdit(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name', 'is_active']

#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         username = self.cleaned_data.get("username")
#         if User.objects.exclude(username=username).filter(email=email).exists():
#             raise forms.ValidationError("El email ya está en uso.")
#         return email
