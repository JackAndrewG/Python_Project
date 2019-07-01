from rest_framework import serializers
from app1.models import Complejo, Cancha
from django.contrib.auth.models import User 

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class ComplejoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Complejo
        fields = ('nombre_complejo', 'direccion_complejo', 'telefono_complejo', 'puntuacion_complejo')

class CanchaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cancha
        fields = ('descripcion_cancha', 'valor_dia', 'valor_noche', 'estado_cancha', 'complejo_id')