from rest_framework import serializers
from core.models import Aluno, Formacao

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'dt_nascimento']

class FormacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formacao
        fields = '__all__'