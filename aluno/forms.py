from django import forms

from aluno.models import Aluno


class AlunoForm(forms.ModelForm):

	class Meta:
		model = Aluno
		fields = 'id_aluno','nome', 'sobrenome', 'nascimento', 'cpf', 'img'
