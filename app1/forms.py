from django import forms

from .models import Cancha, Reserva

class CanchaForm(forms.ModelForm):

    class Meta:
        model = Cancha
        fields = ('descripcion_cancha', 'valor_dia', 'valor_noche', 'foto_cancha',)

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ('usuario', 'cancha', 'fecha_reserva', 'hora_inicio', 'hora_fin', 'valor_unitario', 'valor_total', 'estado_reserva')