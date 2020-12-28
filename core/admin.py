from django.contrib import admin

from .models import Curso, Usuario, Aluno, Formacao

class Cursos(admin.ModelAdmin):
    search_fields = ('nome',)
    list_per_page = 20

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'rg', 'dt_nascimento')
    list_display_link = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 28

class Formacoes(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_link = ('id', 'nome', 'codigo_curso')
    search_fields = ('codigo_curso',)

admin.site.register(Curso, Cursos)
admin.site.register(Usuario)

admin.site.register(Aluno, Alunos)
admin.site.register(Formacao, Formacoes)