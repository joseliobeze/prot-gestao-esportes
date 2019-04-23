from django.db import models
from datetime import date


# Create your models here.
class Aluno(models.Model):
    id_aluno = models.AutoField('Id do Aluno', primary_key=True)
    num_matricula = models.CharField('Matricula', max_length=50, blank=True)
    nome = models.CharField('Nome', max_length=30, blank=False)
    sobrenome = models.CharField('Sobre Nome', max_length=100, blank=False)
    nascimento = models.DateField('Nascimento', auto_now_add=False)    
    data_cadastro = models.DateTimeField('Cadastrado em', auto_now_add=True)
    data_atualização = models.DateTimeField('Atualizado em', auto_now=True)


    @property
    def idade(self):
        hoje = date.today()
        idade = hoje.year - self.nascimento.year - ((hoje.month, hoje.day) < (self.nascimento.month, self.nascimento.day))
        return idade
     
    @property
    def nome_completo(self):
        "Retorna o nome completo do aluno"
        return f'{self.nome} {self.sobrenome}'

    class Meta:
        ordering = ['nome']
        verbose_name = 'Alunos'
        verbose_name_plural = 'Alunos'
    
    def __str__(self):
        return self.nome_completo