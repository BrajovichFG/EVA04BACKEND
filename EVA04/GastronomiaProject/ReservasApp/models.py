from django.db import models

class EstadoReserva(models.Model):
    nombre_estado = models.CharField(max_length=50)  

    def __str__(self):
        return self.nombre_estado

class Reserva(models.Model):
    nombre_reserva = models.CharField(max_length=100)  
    telefono = models.IntegerField()
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    cantidad_personas = models.IntegerField()
    estado = models.ForeignKey(EstadoReserva, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=50)
