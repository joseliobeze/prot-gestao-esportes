# Generated by Django 2.2 on 2019-04-23 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id_aluno', models.AutoField(primary_key=True, serialize=False, verbose_name='Id do Aluno')),
                ('num_matricula', models.CharField(blank=True, max_length=50, verbose_name='Matricula')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=100, verbose_name='Sobre Nome')),
                ('nascimento', models.DateField(verbose_name='Nascimento')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado em')),
                ('data_atualização', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Alunos',
                'verbose_name_plural': 'Alunos',
                'ordering': ['nome'],
            },
        ),
    ]