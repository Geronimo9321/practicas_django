from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import FormularioRegistroUsuario

# Create your views here.
class RegistroUsuario(CreateView):
    template_name = 'usuario/registro.html'
    form_class = FormularioRegistroUsuario
    success_url = reverse_lazy('usuario:path_login')