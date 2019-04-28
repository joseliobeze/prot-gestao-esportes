from django.test import TestCase
from .models import Aluno
from datetime import date


class AlunoModelsTest(TestCase):
    def test_metodo_contaAlunos(self):
        aluno=Aluno(nascimento=date(2000,1,1))
        aluno.save()
        self.assertEqual(1, int(aluno.contAlunos))        
        aluno.delete()
        self.assertEqual(0, int(aluno.contAlunos))


    def test_metodo_idade(self):
        aluno=Aluno(nascimento=date(2000,1,1))
        self.assertEqual(19, int(aluno.idade))
        
 
    def test_mostra_string(self):
        aluno=Aluno(nome='Joselio', sobrenome='Silva')
        self.assertEqual(str(aluno), f'{aluno.nome} {aluno.sobrenome}')


    def test_class_meta(self):
        self.assertEqual(['nome'], Aluno._meta.ordering)
        self.assertEqual('aluno', str(Aluno._meta.verbose_name))
        self.assertEqual('alunos', str(Aluno._meta.verbose_name_plural))