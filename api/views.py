from rest_framework import viewsets
from api.serializer import UserSerializer, ComplejoSerializer, CanchaSerializer
from django.contrib.auth.models import User
from app1.models import Complejo, Cancha

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ComplejoViewSet(viewsets.ModelViewSet):
    queryset = Complejo.objects.all()
    serializer_class = ComplejoSerializer

class CanchaViewSet(viewsets.ModelViewSet):
    queryset = Cancha.objects.filter(complejo=1)
    serializer_class = CanchaSerializer

