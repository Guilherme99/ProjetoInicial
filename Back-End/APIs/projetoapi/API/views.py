from rest_framework import viewsets
from .serializers import UsuarioSerializer
from .models import Usuario
from rest_framework import generics
  
class ListCreateUser(generics.ListCreateAPIView):
    queryset = Usuario.objetos.all()
    serializer_class = UsuarioSerializer


class UpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objetos.all()
    serializer_class = UsuarioSerializer
