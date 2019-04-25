from django.db import models
from datetime import date


TIPO_SEXO = [
    ('FEM', 'Feminino'),
    ('MASC', 'Masculino')
    ]


class Endereços(models.Model):
    pass

class PaisResponsaveis(models.Model):
    pass

class Aluno(models.Model):  
    id_aluno = models.AutoField('Id do Aluno', primary_key=True)
    num_matricula = models.CharField('Matricula', max_length=50, blank=True)
    nome = models.CharField('Nome', max_length=30, blank=False)
    sobrenome = models.CharField('Sobre Nome', max_length=100, blank=False)
    nascimento = models.DateField('Nascimento', auto_now_add=False)    
    rg = models.IntegerField('RG/Certidão de nascimento', blank=True, null=True)
    cpf = models.IntegerField('CPF', blank=True, null=True)
    sexo = models.CharField('Sexo', max_length=4, choices=TIPO_SEXO, blank=True, null=True)
    altura = models.DecimalField('Altura', max_digits=8, decimal_places=2, default=0, blank=True, null=True)
    peso = models.DecimalField('Peso', max_digits=8, decimal_places=4, default=0, blank=True, null=True)
    tipo_sanguinio = models.CharField('Tipo Sanguinio', max_length=11, blank=True, null=True)
    cep = models.IntegerField('Cep', blank=True, null=True)
    estado = models.CharField('Estado', max_length=30, blank=True, null=True, default='')
    cidade = models.CharField('Estado', max_length=50, blank=True, null=True, default='')
    rua = models.CharField('Estado', max_length=50, blank=True, null=True, default='')
    data_cadastro = models.DateTimeField('Cadastrado em', auto_now_add=True)
    data_atualizacão = models.DateTimeField('Atualizado em', auto_now=True)


    @property
    def contAlunos(self):
        """ Conta a quantidade de aluno: Obs.. ainda não foi testada """
        cadastros=Aluno.objects.all()
        return cadastros.count()

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