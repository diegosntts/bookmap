from rest_framework import serializers
from ...models import Curso

class CursoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Curso
            fields = ('id', 'titulo', 'autor', 'editora', 'categoria', 'tipo_obra', 'd_inicio', 'documento', 'status')