from django.contrib import admin
from .models import Reserva, Cancha, Complejo, Suscripcion

admin.site.register(Reserva)
admin.site.register(Cancha)
admin.site.register(Complejo)
admin.site.register(Suscripcion)
