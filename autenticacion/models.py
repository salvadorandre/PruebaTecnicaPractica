from django.db import models

# Create your models here.
class Tareas(models.Model): 
    nombre = models.CharField(max_length=100)
    fecha_vencimiento = models.DateField()
    prioridad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

