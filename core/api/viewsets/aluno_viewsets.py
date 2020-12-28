from rest_framework import viewsets
from core.models import Aluno, Formacao
from core.api.serializers.aluno_serializer import AlunoSerializer, FormacaoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class FormacaosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Formacao.objects.all()
    serializer_class = FormacaoSerializer
