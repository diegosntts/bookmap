from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from core.models import *
from .forms import CursoForm
from django.core.paginator import Paginator
from django.db.models import Q

def curso(request):
        curso = Curso.objects.all()
        paginator = Paginator(curso, 3)
        page = request.GET.get('page')
        cursos = paginator.get_page(page)
        return render(request, 'index.html', {"cursos": cursos})

def get_queryset(self):
        queryset = super(curso, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search)
            )

        return queryset

def cadastrar_usuario(request):
    if request.method == 'POST':
        form_cadastro = CursoForm(request.POST, request.FILES)
        if form_cadastro.is_valid():
            form_cadastro.save()
            return redirect('index')
    else:
        form_cadastro = CursoForm()
    return render(request, 'form_cadastro.html', {"form_cadastro": form_cadastro} )

def livro(request):
    curso = Curso.objects.all()
    paginator = Paginator(curso, 3)
    page = request.GET.get('page')
    cursos = paginator.get_page(page)
    return render(request, 'livros.html', {"cursos": cursos})

def detalhe_livro(request, curso_id):
    cursos = Curso.objects.get(id=curso_id)
    return render(request, 'detalhe_livro.html', {"cursos": cursos})

def dashboard(request):
    cursos = Curso.objects.all()
    return render(request, 'dashboard.html', {"cursos": cursos})

def cadastro_cliente(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/cadastro.html', {"usuarios": usuarios})

def alunos(request):
    if request.method == 'GET':
        alunos ={'id': 1, 'nome': 'Guilherme'}
        return JsonResponse(alunos)
