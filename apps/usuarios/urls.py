from django.urls import path
from .views import UserLoginView, SearchView

APP_NAME = 'usuarios'

urlpatterns = [
    path('ingresar/', UserLoginView.as_view(), name='ingresar'),

    # motor de busqueda
    path('search/', SearchView.as_view(), name='search'),
]
