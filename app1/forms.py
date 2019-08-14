from django import forms

from .models import Cancha, Reserva, Complejo

class ComplejoForm(forms.ModelForm):

    class Meta:
        model = Complejo
        fields = ('nombre_complejo', 'direccion_complejo', 'telefono_complejo', 'foto_complejo', 'coordenadas_complejo', 'hora_apertura', 'hora_cierre')
        widgets = {
            'nombre_complejo': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_complejo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_complejo': forms.TextInput(attrs={'class': 'form-control'}),
            #'foto_complejo': forms.FileInput(attrs={'class': 'form-control'}),
            'coordenadas_complejo': forms.TextInput(attrs={'class': 'form-control'}),
            'hora_apertura': forms.TimeInput(attrs={'class': 'form-control'}),
            'hora_cierre': forms.TimeInput(attrs={'class': 'form-control'}),
        }

class CanchaForm(forms.ModelForm):

    class Meta:
        model = Cancha
        fields = ('descripcion_cancha', 'valor_dia', 'valor_noche', 'foto_cancha', 'estado_cancha')
        widgets = {
        	'descripcion_cancha': forms.TextInput(attrs={'class': 'form-control'}),
        	'valor_dia': forms.NumberInput(attrs={'class': 'form-control'}),
        	'valor_noche': forms.NumberInput(attrs={'class': 'form-control'}),
        #	'foto_cancha': forms.FileInput(attrs={'class': 'form-control'}),
        }

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ('usuario', 'cancha', 'fecha_reserva', 'hora_inicio', 'hora_fin', 'valor_unitario', 'valor_total', 'estado_reserva')