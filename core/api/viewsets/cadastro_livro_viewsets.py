from rest_framework import viewsets
from rest_framework.response import Response
# Modelo
from core.models import Curso
from core.api.serializers.cadastro_livro_serializer import CursoSerializer


class CursosViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Curso.objects.all()
        serializer = CursoSerializer(queryset, many=True)
        return Response(serializer.data)
