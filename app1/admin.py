from django.contrib import admin
from .models import Reserva, Cancha, Complejo, Suscripcion


class ComplejoAdmin(admin.ModelAdmin):
    list_display=('usuario', 'nombre_complejo', 'telefono_complejo', 'puntuacion_complejo', 'estado_complejo')
    list_filter=('estado_complejo',)
    # search_fields=('nombre_complejo',)
class ReservaAdmin(admin.ModelAdmin):
    list_display=('usuario', 'cancha', 'fecha_reserva', 'hora_inicio', 'hora_fin', 'valor_total', 'estado_reserva')
    list_filter=('estado_reserva','fecha_creacion')
    date_hierarchy="fecha_creacion"
    # search_fields=('cancha',)

# titulos
admin.site.site_header = "ADMINISTRACIÓN DE FUTBOLITO"
admin.site.index_title = "FUTBOLITO"
admin.site.site_title = "ADMINISTRACIÓN"

admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Cancha)
admin.site.register(Complejo, ComplejoAdmin)
admin.site.register(Suscripcion)
