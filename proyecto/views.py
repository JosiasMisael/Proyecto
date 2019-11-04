
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, render_to_response
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def frontend(request):
    return render(request,'registration/login.html')
@login_required
def home(request):
    return render(request,'biblioteca/base.html')
#===============================Autor=================================
@login_required
def autor(request):
    autor = Autor.objects.all()
    return render(request,'biblioteca/autor_index.html', {'autor': autor})
@login_required
def autor_nuevo(request):
    if request.method == 'POST':
        form = AutorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('autor_index')         
    else:
        form = AutorForm()
    return render(request, 'biblioteca/autor_edit.html', {'form': form})
@login_required
def autor_edit(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        form = AutorForm(request.POST, request.FILES, instance=autor)
        if form.is_valid():
            autor = form.save(commit=False)
            autor.save()
            return redirect('autor_index')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'biblioteca/autor_edit.html', {'form': form})
@login_required
def autor_show(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'biblioteca/autor_show.html', {'autor': autor})

@login_required
def autor_remove(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    autor.delete()
    return redirect('autor_index')


#===============================Pais=================================
@login_required
def pais(request):
    pais = Pais.objects.all()
    return render(request,'biblioteca/pais_index.html', {'pais':pais})
@login_required
def pais_nuevo(request):
    form = PaisForm()

    if request.method == "POST":
        form = PaisForm(data=request.POST)
        if form.is_valid():
            nombre = form.save(commit=False)
            nombre.save()
            return redirect('pais_index')
    else:
        form = PaisForm()
        return render(request, 'biblioteca/pais_edit.html', {'form':form})
@login_required
def pais_edit(request, pk):
    pais = get_object_or_404(Pais, pk=pk)
    if request.method == "POST":
        form = PaisForm(request.POST,  instance=pais)
        if form.is_valid():
            pais = form.save(commit=False)
            pais.save()
            return redirect('pais_index')
    else:
        form = PaisForm(instance=pais)
    return render(request, 'biblioteca/pais_edit.html', {'form': form})
@login_required
def pais_show(request, pk):
    pais = get_object_or_404(Pais, pk=pk)
    return render(request, 'biblioteca/pais_show.html', {'pais': pais})
@login_required
def pais_remove(request, pk):
    pais = get_object_or_404(Pais, pk=pk)
    pais.delete()
    return redirect('pais_index')


#===============================Libro=================================
@login_required
def libro(request):
    libro = Libro.objects.all()
    return render(request,'biblioteca/libro_index.html', {'libro': libro})
    

@login_required
def libro_nuevo(request):
    if request.method == "POST":
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            libro = Libro.objects.create(titulo=form.cleaned_data['titulo'],editoria=form.cleaned_data['editoria'], categoria=form.cleaned_data['categoria'],unidad=form.cleaned_data['unidad'],precio=form.cleaned_data['precio'],publicacion=form.cleaned_data['publicacion'], image=form.cleaned_data['image'])
            for autor_id in request.POST.getlist('autor'):
                asignacion=Asignacion(autor_id=autor_id, libro_id=libro.id)
                asignacion.save()
                return redirect('libro_index')
    else:
        form = LibroForm()
    return render(request, 'biblioteca/libro_edit.html', {'form': form})


@login_required
def libro_editar(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == "POST":
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.save()
            return redirect('libro_index')

    else:
        form = LibroForm(instance=libro)
    return render(request, 'biblioteca/libro_edit.html', {'form': form})

@login_required
def libro_remove(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    libro.delete()
    return redirect('libro_index')




#===============================Categoria=================================
@login_required
def categoria(request):
    categoria = Categoria.objects.all()
    return render(request,'biblioteca/categoria_index.html', {'categoria': categoria})
@login_required
def categoria_nuevo(request):
    form = CategoriaForm()

    if request.method == "POST":
        form = CategoriaForm(data=request.POST)
        if form.is_valid():
            nombre = form.save(commit=False)
            nombre.save()
            return redirect('categoria_index')
    else:
        form = CategoriaForm()
        return render(request, 'biblioteca/categoria_edit.html', {'form':form})

@login_required
def categoria_edit(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST,  instance=categoria)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            return redirect('categoria_index')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'biblioteca/categoria_edit.html', {'form': form})
@login_required
def categoria_show(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'biblioteca/categoria_show.html', {'categoria': categoria})
@login_required
def categoria_remove(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.delete()
    return redirect('categoria_index')
