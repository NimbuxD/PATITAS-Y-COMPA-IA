from django.shortcuts import render

from .models import Accesorio

# Create your views here.

def index(request):
    context = {}
    return render(request, 'patitasYCompania/index.html', context)

def listar_accesorios(request):
    accesorios = Accesorio.objects.all()
    return render(request, 'patitasYCompania/lista_accesorios.html', {'accesorios': accesorios})