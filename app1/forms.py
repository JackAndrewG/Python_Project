from django import forms

from .models import Cancha, Reserva

class CanchaForm(forms.ModelForm):

    class Meta:
        model = Cancha
        fields = ('codigo_cancha', 'descripcion_cancha', 'valor_dia', 'valor_noche',)

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ('usuario', 'cancha', 'codigo_reserva', 'fecha_reserva', 'hora_reserva', 'valor_untario', 'valor_total', 'estado_reserva',)
