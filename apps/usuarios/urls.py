from django.urls import path
from .views import UserLoginView

APP_NAME = 'usuarios'

urlpatterns = [
    path('ingresar/', UserLoginView.as_view(), name='ingresar'),
]
