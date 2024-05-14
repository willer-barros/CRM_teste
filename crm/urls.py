from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('inicio/', views.inicio, name='inicio'),
    path('usuarios_ativos/', views.usuarios_ativos, name='usuarios_ativos'),
]
