from rest_framework import viewsets
from django.conf import settings
from rest_framework import generics
from ...models import Usuario
# Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
# Classe
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Modelo
from core.api.serializers.usuario_serializer import UsuarioSerializer

class UsuariosViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)

    def list(self, request):
        queryset = Usuario.objects.all()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        serialize = UsuarioSerializer(request.data)
        user = Usuario(nome=serialize.data['nome'], email=serialize.data['email'], senha=serialize.data['senha'])
        user.save()
        return Response('Okay')
