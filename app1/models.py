from django.db import models
from .validators import valid_extension
# Create your models here.

class Complejo (models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre_complejo = models.CharField(max_length=40, default='Complejo Deportivo')
    direccion_complejo = models.TextField(max_length=200, default='sector-calle principal-calle secundaria-nro-referencia')
    telefono_complejo = models.CharField(max_length=19, default='(+593) 098-234-1334')
    puntuacion_complejo = models.IntegerField(default='5')
    foto_complejo = models.ImageField(upload_to='images/complejos_images', null=True, blank=True, validators=[valid_extension])
    coordenadas_complejo = models.CharField(max_length=250, null=True, blank=True)
    hora_apertura = models.TimeField(default='09:00')
    hora_cierre = models.TimeField(default='23:00')
    estado_complejo = models.BooleanField(default = True)

    def Publish(self):
        cadena = "{0}"
        return cadena.format(self.nombre_complejo)

    def __str__(self):
        return self.Publish()

class Cancha (models.Model):
    complejo = models.ForeignKey(Complejo, on_delete=models.CASCADE)
    descripcion_cancha = models.CharField(max_length=200, default='Cancha de fútbol Nro 1')
    valor_dia = models.DecimalField(max_digits=7, decimal_places=2)
    valor_noche = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    foto_cancha = models.ImageField(upload_to='images/canchas_images', null=True, blank=True, validators=[valid_extension])
    estado_cancha = models.BooleanField(default = True)

    def Publish(self):
        cadena = "{0}"
        return cadena.format(self.descripcion_cancha)

    def __str__(self):
        return self.Publish()

class Reserva (models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField(default='12:00')
    hora_fin = models.TimeField(default='13:00')
    valor_unitario = models.DecimalField(max_digits=7, decimal_places=2)
    valor_total = models.DecimalField(max_digits=7, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now = True)
    estado_reserva = models.BooleanField(default=True)

    def Publish(self):
        cadena = "{0}, {1}"
        return cadena.format(self.usuario, self.fecha_reserva)

    def __str__(self):
        return self.Publish()


class Suscripcion (models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    complejo = models.ForeignKey('Complejo', on_delete=models.CASCADE)
    comentario = models.TextField(max_length=354, null=True)
    puntuacion_usuario = models.IntegerField(default='5')
    fecha_creacion = models.DateTimeField(auto_now = True)
    suscripcion = models.BooleanField(default=False, null=True)

    def Publish(self):
        cadena = "{0}, {1}, {2}"
        return cadena.format(self.usuario, self.puntuacion_usuario, self.comentario )

    def __str__(self):
        return self.Publish()