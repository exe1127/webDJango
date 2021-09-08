from django.contrib.auth.models import User
from django.shortcuts import render
from apps.usuarios.models import Usuario

def inicio(request):
    template_name = "inicio.html"

    usuarios = Usuario.objects
    context = {
        'usuarios': usuarios
    }

    return render(request, template_name, context)

def contacto(request):
    template_name = "contacto.html"

    context = {}
      
    return render(request, template, context)

