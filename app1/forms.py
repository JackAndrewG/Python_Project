from django import forms

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
