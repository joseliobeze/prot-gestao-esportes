from django.db import models
from datetime import date


TIPO_SEXO = [
    ('FEM', 'Feminino'),
    ('MASC', 'Masculino')
]


class Aluno(models.Model):
    id_aluno = models.AutoField('Id do Aluno', primary_key=True)
    nome = models.CharField('Nome', max_length=30, blank=False, null=False)
    sobrenome = models.CharField(
        'Sobre Nome', max_length=100, blank=False, null=False)
    nascimento = models.DateField('Nascimento', auto_now_add=False)
    rg = models.CharField('Rg/Registro', max_length=50, blank=True, null=True)
    cpf = models.CharField(
        'CPF', unique=True, max_length=14, blank=True, null=True)
    sexo = models.CharField(
        max_length=4, choices=TIPO_SEXO, blank=True, null=True)
    altura = models.DecimalField(
        'Altura', max_digits=8, decimal_places=2, default=0, blank=True, null=True)
    peso = models.DecimalField(
        'Peso', max_digits=8, decimal_places=4, default=0, blank=True, null=True)
    tipo_sanguinio = models.CharField(
        'Tipo Sanguinio', max_length=11, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fone1 = models.CharField('Telefone', max_length=14, blank=True, null=True)
    fone2 = models.CharField('Celular', max_length=14, blank=True, null=True)
    fone3 = models.CharField('Whatsapp', max_length=14, blank=True, null=True)
    pai = models.CharField(max_length=100, blank=True, null=True)
    fone4 = models.CharField('Telefone', max_length=14, blank=True, null=True)
    mae = models.CharField('Mãe', max_length=100, blank=True, null=True)
    fone5 = models.CharField('Telefone', max_length=14, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True, default='')
    cidade = models.CharField(max_length=50, blank=True, null=True, default='')
    bairro = models.CharField(max_length=50, blank=True, null=True, default='')
    rua = models.CharField(max_length=50, blank=True, null=True, default='')
    img = models.ImageField(upload_to='aluno/images/',
                            verbose_name='Foto', null=True,  blank=True,)
    data_cadastro = models.DateTimeField('Cadastrado em', auto_now_add=True)
    data_atualizacao = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.nome_completo

    class Meta:
        ordering = ['nome']

    @property
    def total_alunos(self):
        """ Conta a quantidade de aluno """
        cadastros = Aluno.objects.all()
        return cadastros.count()

    @property
    def idade(self):
        " Retorna a idade."
        hoje = date.today()
        idade = hoje.year - self.nascimento.year - \
            ((hoje.month, hoje.day) < (self.nascimento.month, self.nascimento.day))
        return idade

    @property
    def nome_completo(self):
        "Retorna o nome completo do aluno"
        return '{} {}'.format(self.nome, self.sobrenome)

    def delete(self, *args, **kwargs):
        self.img.delete()
        super().delete(*args, **kwargs)
