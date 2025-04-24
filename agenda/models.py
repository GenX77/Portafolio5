# agenda/models.py

from django.db import models

class Recordatorio(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField()
    hora = models.TimeField()
    hecho = models.BooleanField(default=False)  # Campo agregado
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.fecha} {self.hora}"
