from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,'biblioteca/base.html')

def autor(request):
    return render(request,'biblioteca/autor_index.html')


def pais(request):
    return render(request,'biblioteca/pais_index.html')


def libro(request):
    return render(request,'biblioteca/libro_index.html')

    
def categoria(request):
    return render(request,'biblioteca/categoria_index.html')