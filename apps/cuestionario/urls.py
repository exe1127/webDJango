from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('home/', home, name='home'),
    path('agregarPreguntas/', agregarPreguntas, name='agregarPreguntas'),
    path('listar/', ListarPreguntas.as_view(), name='listar'),
    path('editar/<int:pk>/', EditarPregunta.as_view(), name='editar')
]
