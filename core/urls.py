from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from core.views import *
urlpatterns = [
    path('', curso, name='index'),
    path('cadastro_usuario', cadastrar_usuario, name='cadastro'),
    path('livros', livro, name='livros'),
    path('<int:curso_id>', detalhe_livro, name='detalhe_livro'),
    path('dasboard', dashboard, name='dashboard'),
    path('cadastro_cliente', cadastro_cliente, name='cadastro_cliente'),
]