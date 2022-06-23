from django.db import models

# Create your models here.


class Info(models.Model):
    empresa = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    nit = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})" #"{nombre de la empresa} ({telefono})"
        return texto.format(self.empresa, self.telefono)