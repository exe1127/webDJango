from django.contrib import admin

from .models import Usuario


class UsuariosAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'email', 'puntos']


admin.site.register(Usuario, UsuariosAdmin)
