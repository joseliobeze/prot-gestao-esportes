from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


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

	return render(request, 'aluno/listaluno.html', {'alunos': alunos})


@login_required
def cadastro(request):
	if request.method == 'POST':
		form = AlunoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.info(request, 'Aluno Cadastro com sucesso')
			return redirect('/aluno/listaluno')
	else:
		form = AlunoForm()
	return render(request, 'aluno/cadastro.html', {'form':form})


@login_required
def EditarCadastro(request, id_aluno):

	aluno = get_object_or_404(Aluno, pk=id_aluno)
	if request.method == "POST":
		form = AlunoForm(request.POST, request.FILES, instance
			= aluno)

		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			messages.info(request,'Cadastro atualizado com sucesso.')
			return redirect('/aluno/listaluno')
		
	else:
		form = AlunoForm(instance=aluno)
	return render(request, 'aluno/editcadastro.html', {'form':form})


@login_required
def DeleteAluno(request, id_aluno):
	aluno = get_object_or_404(Aluno, pk=id_aluno)
	aluno.delete()
	messages.info(request, 'Aluno deletado com sucesso.')
	return redirect('/aluno/listaluno')

@login_required
def VisualizaAluno(request, pk):
	forms =  Aluno.objects.filter(pk=pk)
	return render(request, 'aluno/visualizaluno.html', {'forms':forms})