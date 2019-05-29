from django.contrib import admin
from .models import Aluno, FichaTecnica, FichaMedica

# Register your models here.
admin.site.register(Aluno)
admin.site.register(FichaTecnica)
admin.site.register(FichaMedica)