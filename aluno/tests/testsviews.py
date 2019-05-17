from django.test import TestCase
from aluno.views import ListaAlunos, cadastro
from aluno.models import Aluno

class ViewsAlunosTest(TestCase):
	def setup_test(self):
		aluno = Aluno() 
		pass


	def cadastro_view_test(self):
		""" teste se esta passando o cadastro sem fazer logim 
		>>> c=Cliente()
		esperado codigo 302
		esse teste tem que ser feito antes de fazer login no sistema
		"""	
		pass

		aluno = Aluno(nome="marcos")
		pass