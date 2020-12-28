from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        exclude = ('dt_cadastro', )
        fields = '__all__'