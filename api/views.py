from rest_framework import viewsets
from api.serializer import UserSerializer, ComplejoSerializer
from django.contrib.auth.models import User
from app1.models import Complejo

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ComplejoViewSet(viewsets.ModelViewSet):
    queryset = Complejo.objects.all()
    serializer_class = ComplejoSerializer
