from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)
    email = models.EmailField()
    actividadEconomica = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    ingresos = models.DecimalField(max_digits=10, decimal_places=2)
    pasivos = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Solicitud(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estadosSolicitud = {
        'cancelada': 'Cancelada',
        'aprobada': 'Oferta aprobada',
        'en_espera': 'En espera oferta',
        'creada': 'Oferta creada',
        'finalizada': 'Finalizado',
    }
    estadoSolicitud = models.CharField(choices=estadosSolicitud, max_length=50)
    fecha = models.DateField(default=None)
