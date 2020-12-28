from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from core.api.viewsets.aluno_viewsets import AlunosViewSet
from core.api.viewsets.usuario_viewsets import UsuariosViewSet
from core.api.viewsets.cadastro_livro_viewsets import CursosViewSet
from core.api.viewsets.aluno_viewsets import FormacaosViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UsuariosViewSet, basename='usuarios')
router.register(r'livros', CursosViewSet, basename='livros')
router.register(r'alunos', AlunosViewSet, basename='Alunos')
router.register(r'formacaos', FormacaosViewSet, basename='Formacaos')

urlpatterns = [
    path('', include(router.urls)),
]