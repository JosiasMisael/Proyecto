from django.shortcuts import render, HttpResponse
from .models import Pais, Libro, Autor, Categoria

# Create your views here.

def home(request):
    return render(request,'biblioteca/base.html')

def autor(request):
    autor = Autor.objects.all()
    return render(request,'biblioteca/autor_index.html', {'autor': autor})


def pais(request):
    pais = Pais.objects.all()
    return render(request,'biblioteca/pais_index.html', {'pais':pais})


def libro(request):
    return render(request,'biblioteca/libro_index.html')

    
def categoria(request):
    categoria = Categoria.objects.all()
    return render(request,'biblioteca/categoria_index.html', {'categoria': categoria})