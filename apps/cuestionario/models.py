from django.db import models


class Cuestionario(models.Model):
    pregunta = models.CharField(max_length=200, null=True)
    respuesta1 = models.CharField(max_length=200, null=True)
    respuesta2 = models.CharField(max_length=200, null=True)
    respuesta3 = models.CharField(max_length=200, null=True)
    correcta = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'cuestionario'

    def __str__(self):

        return self.pregunta
