from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import LoginForm

class UserLoginView(TemplateView):
	template_name = 'registration/login.html'

	def post(self, request, *args, **kwargs):
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/') # redirige al usuario a la página de inicio después de iniciar sesión
			else:
				messages.error(request, 'Usuario o contraseña incorrecta.')
		else:
			messages.error(request, 'Por favor, introduce un nombre de usuario y contraseña válidos.')
		return render(request, self.template_name, {'form': form})

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['sub_title'] = "Ingresar"
		context['form'] = LoginForm()
		return context
	