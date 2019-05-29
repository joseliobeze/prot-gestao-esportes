from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db.models import Q

from .models import Aluno
from .forms import AlunoForm


@login_required
def ListaAlunos(request):
    search = request.GET.get('search')
    if search:
        alunos = Aluno.objects.filter(
            Q(nome__icontains=search) | Q(cpf__exact=search))
        tot = alunos
        if not alunos:
            messages.info(request, f'{ search } não encontrado, virifique se digitou NOME ou CPF correto')
    else:
        alunos = Aluno.objects.all().order_by('nome')
        tot = alunos
        if not alunos:
            messages.info(request, 'Ainda não há alunos cadastrados.')

    paginator = Paginator(alunos, 10)
    page = request.GET.get('page')
    aluno_list = paginator.get_page(page)
    return render(request, 'aluno/aluno_list.html', {'aluno_list': aluno_list, 'tot': tot})

@login_required
def cadastro(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():            
            form.save()
            messages.info(request, 'Aluno Cadastro com sucesso')
            return redirect('/aluno/lista')
    else:
        form = AlunoForm()
    return render(request, 'aluno/aluno_cadastro.html', {'form': form})

@login_required
def EditarCadastro(request, id_aluno):

    aluno = get_object_or_404(Aluno, pk=id_aluno)
    if request.method == "POST":
        form = AlunoForm(request.POST, request.FILES, instance=aluno)

        if form.is_valid():

            form.save()
            messages.info(request, 'Cadastro atualizado com sucesso.')
            return redirect('/aluno/lista')

    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'aluno/edita_cadastro.html', {'form': form})

@login_required
def DeleteAluno(request, pk):
    template_name = 'aluno/delete_aluno.html'
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        messages.info(request, 'Aluno deletado com sucesso.')
        return redirect('/aluno/lista')
    return render(request, template_name, {'aluno': aluno})

@login_required
def VisualizaAluno(request, pk):
    forms = Aluno.objects.filter(pk=pk)
    return render(request, 'aluno/aluno_detalhes.html', {'forms': forms})
