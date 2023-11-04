from django.urls import path
from .views.inicio.views import Inicio

APP_NAME = 'landingpage'

urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
]