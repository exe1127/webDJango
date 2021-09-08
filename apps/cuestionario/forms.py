from django.forms import ModelForm
from .models import *


class agregarPreguntas(ModelForm):
    class Meta:
        model = Cuestionario
        fields = "__all__"
