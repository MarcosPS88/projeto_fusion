from django.contrib import admin
from .models import Funcionario, Servico, Cargo, Recurso


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome',
                    'criado',
                    'modificado',
                    'ativo'
                    )


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico',
                    'icone',
                    'criado',
                    'modificado',
                    'ativo'
                    )


@admin.register(Cargo)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('cargo',
                    'criado',
                    'modificado',
                    'ativo'
                    )


@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('nome',
                    'modificado'
                    )
