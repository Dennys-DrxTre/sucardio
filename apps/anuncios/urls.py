from django.urls import path
from .views import Base

APP_NAME = 'anuncio'

urlpatterns = [
    path('base/', Base.as_view(), name='base'),
]
