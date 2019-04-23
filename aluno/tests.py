from django.test import TestCase
from .models import Aluno
from datetime import date


class AlunoTestCase(TestCase):
    def setUp(self):
        self.aluno = Aluno()
        #self.aluno1 = Aluno.objects.create(nome='Joselio', sobrenome='Silva', nascimento= '2000-9-28')
        self.aluno.nome = 'Joselio'
        self.aluno.sobrenome = 'Silva'
        self.aluno.nascimento = date(2000,9,28)


    def testnome_completo(self):
        self.assertEquals(self.aluno.nome_completo,'Joselio Silva')

    def testnascimento(self):
        self.assertEquals(self.aluno.nascimento, date(2000,9,28))

    def testidade(self):
        self.assertEquals(self.aluno.idade, 18)