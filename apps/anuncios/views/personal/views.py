from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from ...forms import PersonalForm, UserForm
from django.views.generic import (
	TemplateView,
	ListView
)
from ...models import Usuario
from django.contrib.auth.models import User


class ListadoPersonal(LoginRequiredMixin, ListView):
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

class RegistrarPersonal(LoginRequiredMixin, TemplateView):
	template_name = 'pages/personal/registrar_personal.html'

	def post(self, request, *args, **kwargs):
		try:
			form = UserForm(request.POST)
			if form.is_valid():
				if not User.objects.filter(username = form.cleaned_data['cedula']).exists():
					form.save()
					
					user = User.objects.get(username = form.cleaned_data['cedula'])
					# permissions = Permission.objects.filter(codename__in=group_permissions_choices[form.cleaned_data['role']])
					# for permission in permissions:
					# 	user.user_permissions.add(permission)
					# user.save()

					rol = UserSecurity()
					rol.workstation = form.cleaned_data['role']
					rol.user_id = user.pk
					rol.save()
					
				else:
					data['response'] = {'title':'Ocurrió un error!', 'data': 'El usuario ya esta registrado', 'type_response': 'danger'}
			else:
				for field, errors in form.errors.items():
					for error in errors:
						data['response'] = {'title':field, 'data': error, 'type_response': 'danger'}
		except Exception as e:
			data['error'] = str(e)
		return JsonRresponse(data, safe=False)
							
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["title"] = "Personal"
		context["sub_title"] = "Registrar personal"
		context["form"] = PersonalForm()
		return context