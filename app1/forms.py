from django import forms

<<<<<<< HEAD
from .models import Complejo

class ComplejoForm(forms.ModelForm):

    class Meta:
        model = Complejo

        fields = [
            'nombre_complejo',
            'direccion_complejo',
            'telefono_complejo',
        ]
        labels = {
            'nombre_complejo': 'Nombre de Complejo Deportivo',
            'direccion_complejo': 'Dirección de complejo deportivo',
            'telefono_complejo': 'Teléfono de complejo deportivo',

        }
        widgets= {
            'nombre_complejo': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_complejo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_complejo': forms.TextInput(attrs={'class': 'form-control'}),
        }
=======
from .models import Cancha, Reserva

class CanchaForm(forms.ModelForm):

    class Meta:
        model = Cancha
        fields = ('codigo_cancha', 'descripcion_cancha', 'valor_dia', 'valor_noche',)

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ('usuario', 'cancha', 'codigo_reserva', 'fecha_reserva', 'hora_reserva', 'valor_untario', 'valor_total', 'estado_reserva',)
>>>>>>> 8009f5c292c6e19246eeded258f58cb6f00e0595
