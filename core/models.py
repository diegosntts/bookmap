from django.db import models
from django.conf import settings

class Local(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nome')
    latitude = models.IntegerField(null=True, verbose_name='Latitude')
    longitude = models.IntegerField(null=True, verbose_name='Longitude')
    endereco = models.CharField(max_length=100, verbose_name='Endereco')
    urlmapa = models.CharField(max_length=100, verbose_name='Urlmapa')

class Curso(models.Model):
    titulo = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Titulo')
    autor = models.CharField(max_length=100, null=True,
                             blank=True, verbose_name='Autor')
    editora = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Editora')
    categoria = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Categoria')
    tipo_obra = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Tipo de obra')
    d_inicio = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Data inicio')
    documento = models.FileField(
        upload_to='media', null=True, verbose_name='Documento')
    status = models.BooleanField(default=False, verbose_name='status')

    local = models.ForeignKey(Local, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    nome = models.CharField(max_length=100, null=True,
                            blank=True, verbose_name='Nome')
    email = models.CharField(max_length=100, null=True,
                             blank=True, verbose_name='Email')
    senha = models.CharField(max_length=50, null=True,
                             blank=True, verbose_name='Senha')

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    dt_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Formacao(models.Model):
    NIVEL = (
        ('B', 'Basico'),
        ('I', 'Intermediario'),
        ('A', 'Avançado'),
    )
    codigo_curso = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL,
                             blank=False, null=False, default='8')
