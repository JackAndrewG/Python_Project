from rest_framework import viewsets
from api.serializer import UserSerializer, ComplejoSerializer, CanchaSerializer, ReservaSerializer, SuscripcionSerializer
from django.contrib.auth.models import User
from app1.models import Complejo, Cancha, Reserva, Suscripcion

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        if (self.request.query_params.get('email')):
            email = self.request.query_params.get('email')
            return User.objects.filter(email=email)
        elif (self.request.query_params.get('username')):
            username = self.request.query_params.get('username')
            return User.objects.filter(username=username)
        else:
            return self.queryset

class ComplejoViewSet(viewsets.ModelViewSet):
    queryset = Complejo.objects.all()
    serializer_class = ComplejoSerializer

class CanchaViewSet(viewsets.ModelViewSet):
    queryset = Cancha.objects.all()
    serializer_class = CanchaSerializer
    def get_queryset(self):
        if (self.request.query_params.get('complejo')):
            complejo_ID = self.request.query_params.get('complejo')
            return Cancha.objects.filter(complejo=complejo_ID, estado_cancha=1)
        else:
            return self.queryset

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    def get_queryset(self):
        if (self.request.query_params.get('usuario') and self.request.query_params.get('estado')):
            user = self.request.query_params.get('usuario')
            estado = self.request.query_params.get('estado')
            return Reserva.objects.filter(usuario=user, estado_reserva=estado)
        else:
            return self.queryset

class SuscripcionViewSet(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer
    def get_queryset(self):
        if (self.request.query_params.get('complejo')):
            complejo = self.request.query_params.get('complejo')
            return Suscripcion.objects.filter(complejo=complejo)
        else:
            return self.queryset
