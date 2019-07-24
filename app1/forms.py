from django import forms

from .models import Cancha, Reserva, Complejo

class ComplejoForm(forms.ModelForm):

    class Meta:
        model = Complejo
        fields = ('nombre_complejo', 'direccion_complejo', 'telefono_complejo', 'foto_complejo')
        
class CanchaForm(forms.ModelForm):

    class Meta:
        model = Cancha
        fields = ('descripcion_cancha', 'valor_dia', 'valor_noche', 'foto_cancha')
        widgets = {
        	'descripcion_cancha': forms.TextInput(attrs={'class': 'form-control'}),
        	'valor_dia': forms.NumberInput(attrs={'class': 'form-control'}),
        	'valor_noche': forms.NumberInput(attrs={'class': 'form-control'}),
        	'foto_cancha': forms.FileInput(attrs={'class': 'form-control'}),
        }

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ('usuario', 'cancha', 'fecha_reserva', 'hora_inicio', 'hora_fin', 'valor_unitario', 'valor_total', 'estado_reserva')