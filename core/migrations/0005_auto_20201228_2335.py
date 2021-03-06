# Generated by Django 3.1.2 on 2020-12-29 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_aluno_formacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome')),
                ('latitude', models.IntegerField(null=True, verbose_name='Latitude')),
                ('longitude', models.IntegerField(null=True, verbose_name='Longitude')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereco')),
                ('urlmapa', models.CharField(max_length=100, verbose_name='Urlmapa')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='local',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.local'),
        ),
    ]
