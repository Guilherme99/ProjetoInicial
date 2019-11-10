from rest_framework import viewsets
from .serializers import *
from .models import Usuario
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.status import(
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED
)
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class ListUser(generics.ListAPIView):
        queryset = Usuario.objetos.all()
        serializer_class = UsuarioSerializer
class CreateUser(generics.CreateAPIView):
        queryset = Usuario.objetos.all()
        serializer_class = UsuarioSerializer  
class UpdateUser(generics.RetrieveUpdateAPIView):
        queryset = Usuario.objetos.all()
        serializer_class = UsuarioSerializer
class DestroyUser(generics.RetrieveDestroyAPIView):
        queryset = Usuario.objetos.all()
        serializer_class = UsuarioSerializer
class Login(APIView):
        queryset = Usuario.objetos.all()
        serializer_class = LoginSerializer
        def loginserver(x, y):
                userfiltro = Usuario.objetos.filter(usuario=x).filter(senha=y).count()
                if userfiltro==1:
                        return Response(status=HTTP_200_OK)
                return Response(status=HTTP_401_UNAUTHORIZED)
        def post(self,request):
                data = JSONParser().parse(request)
                return Login.loginserver(data['usuario'], data['senha'])
        
