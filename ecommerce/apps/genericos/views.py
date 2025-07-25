from django.shortcuts import render
from .models import Rubro
# Create your views here.

def Listar_Rubros(request):

    rubros = Rubro.objects.all()

    return render(request, 'genericos/rubros.html', {'rubros':rubros})