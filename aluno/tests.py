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

        self.aluno1=Aluno()
        self.aluno1.nome = 'marcelo'
        self.aluno1.sobrenome = 'borges'
        self.aluno1.nascimento = date(2001,10,28)
      


    def testnome_completo(self):
        self.assertEquals(self.aluno.nome_completo,'Joselio Silva')
        self.assertEquals(self.aluno1.nome_completo, 'marcelo borges')

    def testnascimento(self):
        self.assertEquals(self.aluno.nascimento,  date(2000,9,28))
        self.assertEquals(self.aluno1.nascimento,  date(2001,10,28))


    def testidade(self):
        self.assertEquals(self.aluno.idade, 18)
        self.assertEquals(self.aluno1.idade, 17)

        