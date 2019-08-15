from rest_framework import serializers
from app1.models import Complejo, Cancha, Reserva, Suscripcion
from django.contrib.auth.models import User

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'first_name','last_name', 'username', 'email', 'password', 'is_staff')

class ComplejoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Complejo
        fields = ('nombre_complejo', 'direccion_complejo', 'telefono_complejo', 'puntuacion_complejo', 'id', 'foto_complejo', 'coordenadas_complejo')

class CanchaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cancha
        fields = ('id', 'descripcion_cancha', 'valor_dia', 'valor_noche', 'estado_cancha', 'complejo', 'foto_cancha')

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('usuario', 'cancha', 'fecha_reserva', 'hora_inicio', 'hora_fin', 'valor_unitario', 'valor_total', 'fecha_creacion', 'estado_reserva')

class SuscripcionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Suscripcion
        fields = ('usuario', 'complejo', 'comentario', 'puntuacion_usuario', 'fecha_creacion', 'suscripcion')
