from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required


from .models import Aluno
from .forms import AlunoForm

@login_required
def ListaAlunos(request):

	search = request.GET.get('search')
	if search:
		
		aluno1 = Aluno.objects.filter(nome__icontains=search)
		aluno2 = Aluno.objects.filter(cpf__exact=search)
		alunos = aluno1 or aluno2
	else:

		alunos_list = Aluno.objects.all().order_by('nome')

		paginator = Paginator(alunos_list, 3)

		page = request.GET.get('page')

		alunos = paginator.get_page(page)

	return render(request, '/aluno/listaluno.html', {'alunos': alunos})

@login_required
def CadastroAluno(request):

	form = AlunoForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			messages.info(request, 'Aluno Cadastrado com sucesso.')
			return redirect('/aluno/listaluno', {})
	# Retorna a pagina com form vazio ou erros:
	return render(request, 'aluno/cadastralunos.html', {'form': form}, {})

@login_required
def EditarCadastro(request, id_aluno):

	aluno = get_object_or_404(Aluno, pk=id_aluno)
	form = AlunoForm(instance=aluno)
	context = {'form': form, 'aluno':aluno}
	if request.method == "POST":
		form = AlunoForm(request.POST or None, instance
			= aluno)
		if form.is_valid():
			form.save()
			messages.info(request,'Cadastro atualizado com sucesso.')
			return redirect('/aluno/listaluno')
		else:
			return render(request, 'aluno/editcadastro.html', {'form':form, 'aluno':aluno})
	else:
		return render(request, 'aluno/editcadastro.html', context)

@login_required
def DeleteAluno(request, id_aluno):
	aluno = get_object_or_404(Aluno, pk=id_aluno)
	aluno.delete()
	messages.info(request, 'Aluno deletado com sucesso.')
	return redirect('/aluno/listaluno')

@login_required
def VisualizaAluno(request, pk):

	template_name = {}
	template_name['form'] =  get_object_or_404(Aluno, pk=pk)
	return render(request, 'aluno/visualizaluno.html', template_name)