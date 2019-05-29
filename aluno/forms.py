from django import forms

from aluno.models import Aluno


class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'
        exclude = ['id_aluno', 'data_atualizacao']
        widgets = {
            'nome': forms.TextInput(attrs={'id': 'id_nome', 'class': 'form-control', 'maxlength': 30, 'placeholder': 'Ex: João'}),
            'sobrenome': forms.TextInput(attrs={'id': 'id_sobrenome', 'class': 'form-control', 'maxlength': 50, 'placeholder': 'Ex: Figueredo Da Silva'}),
            'nascimento': forms.TextInput(attrs={'id': 'id_nascimento', 'class': 'form-control', 'type': 'date', 'placeholder': 'Ex: dd/mm/aaaa'}),
            'rg': forms.TextInput(attrs={'type': 'number', 'id': 'id_rg', 'class': 'form-control', 'maxlength': 50, 'placeholder': '  RG ou Registro'}),
            'cpf': forms.TextInput(attrs={'type': 'text', 'id': 'id_cpf', 'class': 'form-control', 'onkeypress': "$(this).mask('000.000.000-00')", 'maxlength': 10, 'placeholder': 'Ex: 000.000.000-00'}),
            'sexo': forms.Select(attrs={'type': 'text', 'id': 'id_sexo', 'class': 'form-control', 'maxlength': 9}),
            'altura': forms.NumberInput(attrs={'type': 'number', 'id': 'id_altura', 'class': 'form-control', 'max': 3, 'placeholder': 'Ex: 1,75'}),
            'peso': forms.NumberInput(attrs={'type': 'number', 'id': 'id_peso', 'class': 'form-control', 'max': 250, 'placeholder': 'Ex: 65,50'}),
            'tipo_sanguinio': forms.TextInput(attrs={'type': 'text', 'id': 'id_tipo', 'class': 'form-control', 'maxlength': 4, 'placeholder': 'Ex: A +'}),
            'email': forms.EmailInput(attrs={'type': 'email', 'id': 'id_email', 'class': 'form-control', 'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$', 'placeholder': 'Ex: aluno@gmail.com'}),
            'fone1': forms.TextInput(attrs={'type': 'tel', 'id': 'id_tel1', 'class': 'form-control', 'maxlenght': 14, 'pattern':'(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})', 'onkeypress': "$(this).mask('(00)0000-00009')", 'placeholder': 'Ex: (00)00000-0000'}),
            'fone2': forms.TextInput(attrs={'type': 'tel', 'id': 'id_tel2', 'class': 'form-control', 'maxlenght': 14, 'pattern':'(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})', 'onkeypress': "$(this).mask('(00)0000-00009')", 'placeholder': 'Ex: (00)00000-0000'}),
            'fone3': forms.TextInput(attrs={'type': 'tel', 'id': 'id_tel3', 'class': 'form-control', 'maxlenght': 14, 'pattern':'(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})', 'onkeypress': "$(this).mask('(00)0000-00009')", 'placeholder': 'Ex: (00)00000-0000'}),
            'pai': forms.TextInput(attrs={'type': 'text', 'id': 'id_pai', 'class': 'form-control', 'maxlength': 4, 'placeholder': 'Ex: José Silva Morais '}),
            'fone4': forms.TextInput(attrs={'type': 'tel', 'id': 'id_tel4', 'class': 'form-control phone-mask', 'pattern':'(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})','maxlenght': 12, 'onkeypress': "$(this).mask('(00)0000-00009')", 'placeholder': 'Ex: (00)00000-0000'}),
            'mae': forms.TextInput(attrs={'type': 'text', 'id': 'id_mae', 'class': 'form-control', 'maxlength': 4, 'placeholder': 'Ex: Maria Oliveira'}),
            'fone5': forms.TextInput(attrs={'type': 'tel', 'id': 'id_tel5', 'class': 'form-control phone-mask', 'pattern':'(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})','maxlenght': 12, 'onkeypress': "$(this).mask('(00)0000-00009')", 'placeholder': 'Ex: (00)00000-0000'}),
            'cep': forms.TextInput(attrs={'type': 'tel', 'id': 'id_cep', 'class': 'form-control phone-mask', 'maxlenght': 10, 'pattern':'(\d{5}\-\d{3})', 'onkeypress': "$(this).mask('00000-000')", 'placeholder': 'Ex: 00.000-000'}),
            'estado': forms.TextInput(attrs={'type': 'tel', 'id': 'id_estado', 'class': 'form-control', 'maxlenght': 50, 'placeholder': 'Ex: Maranhão'}),
            'cidade': forms.TextInput(attrs={'type': 'tel', 'id': 'id_cidade', 'class': 'form-control', 'maxlenght': 50, 'placeholder': 'Ex: São Luiz'}),
            'bairro': forms.TextInput(attrs={'type': 'tel', 'id': 'id_bairro', 'class': 'form-control', 'maxlenght': 50, 'placeholder': 'Ex: Quatraque'}),
            'rua': forms.TextInput(attrs={'type': 'tel', 'id': 'id_rua', 'class': 'form-control', 'maxlenght': 17, 'placeholder': 'Ex: Rua Grande ou QD 00, LOT 5'}),
            'img': forms.ClearableFileInput(attrs={'id': 'id_img', 'class': 'custom-file-input', 'type': 'file', 'target': '_blank'}),
        }
