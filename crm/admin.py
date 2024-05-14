from django.contrib import admin
from .models import  Agente, Supervisor


@admin.register(Agente)
class AdminAgente(admin.ModelAdmin):
    model = Agente
    list_display = ('nome', 'cpf')

@admin.register(Supervisor)
class AdminSupervisor(admin.ModelAdmin):
    model = Supervisor
    list_display = ('nome', 'cpf')
