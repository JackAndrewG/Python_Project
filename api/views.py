from rest_framework import viewsets
from api.serializer import UserSerializer
from django.contrib.auth.models import User
from app1.models import Complejo

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
