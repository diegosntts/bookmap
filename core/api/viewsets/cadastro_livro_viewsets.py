from rest_framework import viewsets
# Modelo
from core.models import Curso
from core.api.serializers.cadastro_livro_serializer import CursoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer