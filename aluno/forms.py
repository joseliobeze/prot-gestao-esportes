from django import forms

from aluno.models import Aluno


class AlunoForm(forms.ModelForm):

	class Meta:
		model = Aluno
		fields = 'nome', 'sobrenome', 'nascimento', 'cpf', 'img'
