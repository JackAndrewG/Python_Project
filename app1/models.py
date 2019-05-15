from django.db import models

# Create your models here.

class Complejo (models.Model):
    nombre_complejo = models.CharField(max_length=40, default='Complejo Deportivo ')
    direccion_complejo = models.TextField(max_length=200, default='sector-calle principal-calle secundaria-nro-referencia')
    telefono_complejo = models.CharField(max_length=19, default='(+593) 098-234-1334')
    cantidad_canchas = models.IntegerField()
    puntuacion_complejo = models.IntegerField(default='5')
    estado_complejo = models.BooleanField(default = True)

    def Publish(self):
        cadena = "{0}, {1}, {2}"
        return cadena.format(self.nombre_complejo, self.puntuacion_complejo, self.estado_complejo)


    def __str__(self):
        return self.Publish()

class Cancha (models.Model):
    codigo_cancha = models.CharField(max_length=3, default='001')
    descripcion_cancha = models.TextField(max_length=150, default='cancha de futbolito')
    complejo = models.ForeignKey(Complejo, on_delete=models.CASCADE)
    valor_dia = models.DecimalField(max_digits=7, decimal_places=2)
    valor_noche = models.DecimalField(max_digits=7, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now = True)
    estado_cancha = models.BooleanField(default = True)

    def Publish(self):
        cadena = "{0}, {1}, {2}"
        return cadena.format(self.codigo_cancha, self.descripcion_cancha, self.estado_cancha)


    def __str__(self):
        return self.Publish()


class Reserva (models.Model):
    codigo_reserva = models.CharField(max_length=6, default='000123')
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    #numero_cancha relacionar
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField(default='12:00')
    valor_untario = models.DecimalField(max_digits=7, decimal_places=2)
    valor_total = models.DecimalField(max_digits=7, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now = True)
    estado_reserva = models.BooleanField(default=True)

    def Publish(self):
        cadena = "{0}, {1}, {2}"
        return cadena.format(self.usuario, self.fecha_creacion, self.fecha_reserva)


    def __str__(self):
        return self.Publish()
