from django.contrib import admin
from django.urls import path
from .views import inicio, login, registrarse, contacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('login/', login),
    path('registrarse/', registrarse),
    path('contacto/', contacto)
]


