from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Agente
from django.http import JsonResponse

def index(request):
    return render(request,'index.html')

def inicio(request):
    return render(request,'inicio.html')


def usuarios_ativos(request):
    usuarios_ativos = Agente.objects.filter(ativo= True)
    data = {
        'usuarios': list(usuarios_ativos.values())
    }
    return JsonResponse(data)