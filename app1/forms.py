from django import forms

from .models import Cancha, Reserva, Complejo

class ComplejoForm(forms.ModelForm):

    class Meta:
        model = Complejo
        fields = ('nombre_complejo', 'direccion_complejo', 'telefono_complejo')

class CanchaForm(forms.ModelForm):

    class Meta:
        model = Cancha
        fields = ('codigo_cancha', 'descripcion_cancha', 'valor_dia', 'valor_noche',)

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ('usuario','cancha', 'codigo_reserva', 'fecha_reserva', 'hora_inicio', 'hora_fin', 'valor_unitario', 'valor_total', 'estado_reserva',)