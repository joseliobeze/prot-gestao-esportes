from django.urls import path
from . import views

app_name = 'aluno'
urlpatterns = [
	path('listaluno/', views.ListaAlunos, name='lista-aluno'),
	path('cadastraluno/', views.CadastroAluno, name='cadastro-aluno'),
	path('editcadastro/<int:id_aluno>', views.EditarCadastro, name='edita-cadastro'),
	path('visualizaluno/<int:pk>/', views.VisualizaAluno, name='visualiza-aluno'),
	path('deletaluno/<int:id_aluno>/', views.DeleteAluno, name='delete-aluno'),
]