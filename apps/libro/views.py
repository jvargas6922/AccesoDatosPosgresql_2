from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm

# Create your views here.

def listado_libros(request):
    # libros = Libro.objects.all()
    libros = Libro.objects.filter(deleted_at__isnull=True)  # Traer solo los libros que no están eliminados (deleted_at es null)
    # libro = Libro.objects.get(id_libro=1)
    # libro = Libro.objects.filter(nombre='IT')
    # for l in libro:
    #     print(l.nombre)

    # Traer solo los libros que están eliminados (deleted_at no es null)
    # registros_eliminados = Libro.objects.filter(deleted_at__isnull=False)
    # for libros in registros_eliminados:
    #     restaurar_registro(id_libro=libros.id_libro)  # Restaurar cada libro eliminado
    #     print(f"Libro con ID {libros.id_libro} restaurado.")
    return render(request, 'libro/listado.html', {'libros': libros})

def crear(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('listado_libros')
    return render(request, 'libro/crear.html', {'form': LibroForm()})

def editar(request, id_libro):
    libro = get_object_or_404(Libro, id_libro=id_libro)
    form = LibroForm(instance=libro)
    context = {
        'form': form,
        'libro': libro
    }
    return render(request, 'libro/editar.html', context)

def actualizar(request, id_libro):
    libro = get_object_or_404(Libro, id_libro=id_libro)
    form = LibroForm(request.POST, instance=libro)
    if form.is_valid():
        form.save()
        return redirect('listado_libros')
    context = {
        'form': form,
        'libro': libro
    }
    return render(request, 'libro/editar.html', context)

def eliminar(request, id_libro):
    libro = get_object_or_404(Libro, id_libro=id_libro)
    libro.delete()
    return redirect('listado_libros')

def restaurar_registro(id_libro):
    libro = get_object_or_404(Libro, id_libro=id_libro)
    libro.restore()
    return redirect('listado_libros')