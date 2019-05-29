from django.urls import path
from . import views

app_name = 'aluno'
urlpatterns = [
    path('lista/', views.ListaAlunos, name='lista_aluno'),
    path('editcadastro/<int:id_aluno>',
         views.EditarCadastro, name='edita_cadastro'),
    path('visualizaluno/<int:pk>/', views.VisualizaAluno, name='detalhe_aluno'),
    path('deletaluno/<int:pk>/', views.DeleteAluno, name='delete_aluno'),
    path('cadastro/', views.cadastro, name='cadastro_aluno'),
]
