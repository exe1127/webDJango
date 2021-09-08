from django.contrib import admin
from .models import *


class CuestionariosAdmin(admin.ModelAdmin):
    list_display = ['id', 'pregunta', 'respuesta1',
                    'respuesta2', 'respuesta3', 'correcta']


admin.site.register(Cuestionario, CuestionariosAdmin)
