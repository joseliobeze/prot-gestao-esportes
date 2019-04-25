from django.test import TestCase
from .models import Aluno
from datetime import date


class AlunoTestCase(TestCase):
    def testcampos_models(self):
        """testes de campo e e comportamento das açoes e funções"""
        aluno = Aluno()
        aluno.num_matricula = 'turma12'
        aluno.nome = 'Joselio'
        aluno.sobrenome = 'Silva'
        aluno.nascimento = date(2000,9,28)
        aluno.rg = 123456789
        aluno.cpf = 987654321
        aluno.sexo = 'Masculino'
        aluno.altura = 1.65
        aluno.peso = 45.50
        aluno.tipo_sanguinio = 'AB'
        aluno.email = 'teste@gmail.com'
        
        aluno.cep = 65750000
        aluno.estado = 'GO'
        aluno.cidade = 'Aguas Lindas'
        aluno.rua = 'sem nome'
        aluno.data_cadastro = date.today()
        aluno.data_atualizacão = date.today()
        aluno.save()
      

        self.assertIs(aluno.id_aluno, 1)
        self.assertIs(aluno.num_matricula, 'turma12')
        self.assertEquals(aluno.nome_completo,'Joselio Silva')
        self.assertEquals(aluno.nascimento, date(2000,9,28))
        self.assertIs(aluno.rg, 123456789)
        self.assertEqual(aluno.sexo, 'Masculino')
        self.assertEquals(aluno.idade, 18)
        self.assertIs(aluno.email, aluno.nome)
        self.assertIs(aluno.contAlunos, 1)
        aluno.delete()
        self.assertIs(aluno.contAlunos, 0)

        