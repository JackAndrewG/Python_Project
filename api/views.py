from rest_framework import viewsets
from api.serializer import UserSerializer, ComplejoSerializer, CanchaSerializer
from django.contrib.auth.models import User
from app1.models import Complejo, Cancha
from django.shortcuts import get_object_or_404

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ComplejoViewSet(viewsets.ModelViewSet):
    queryset = Complejo.objects.all()
    serializer_class = ComplejoSerializer

class CanchaViewSet(viewsets.ModelViewSet):
    queryset = Cancha.objects.all()
    serializer_class = CanchaSerializer
    def get_queryset(self):
        complejo_ID = self.request.query_params.get('complejo')
        return Cancha.objects.filter(complejo=complejo_ID)
