from rest_framework import viewsets
from api.serializer import UserSerializer, ComplejoSerializer, CanchaSerializer, ReservaSerializer
from django.contrib.auth.models import User
from app1.models import Complejo, Cancha, Reserva

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        if (self.request.query_params.get('email')):
            email = self.request.query_params.get('email')
            return User.objects.filter(email=email)
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
            return Cancha.objects.filter(complejo=complejo_ID)
        else:
            return self.queryset

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    def get_queryset(self):
        if (self.request.query_params.get('estado')):
            estado = self.request.query_params.get('estado')
            return Reserva.objects.filter(estado_reserva=estado)
        else:
            return self.queryset