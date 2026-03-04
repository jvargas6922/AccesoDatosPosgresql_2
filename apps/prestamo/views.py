from django.shortcuts import render, redirect, get_object_or_404
from .models import Prestamo
from apps.libro.models import Libro
from apps.usuario.models import Usuario
from .forms import PrestamoForm

# Create your views here.
def listado_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamo/listado.html', {'prestamos': prestamos})

def crear(request):
    libros = Libro.objects.all()
    usuarios = Usuario.objects.all()
    if request.method == 'POST':
        form = PrestamoForm(request.POST, libros=libros, usuarios=usuarios)
        if form.is_valid():
            form.save()
            return redirect('listado_prestamos')
    else:
        form = PrestamoForm(libros=libros, usuarios=usuarios)

    context = {
        'form': form,
        'libros': libros,
        'usuarios': usuarios
    }
    return render(request, 'prestamo/crear.html', context)

def editar(request, id_prestamo):
    prestamo = get_object_or_404(Prestamo, id_prestamo=id_prestamo)
    form = PrestamoForm(
        instance=prestamo,
        libros=Libro.objects.all(),
        usuarios=Usuario.objects.all()
    )
    context = {
        'form': form,
        'prestamo': prestamo
    }
    return render(request, 'prestamo/editar.html', context)

def actualizar(request, id_prestamo):
    prestamo = get_object_or_404(Prestamo, id_prestamo=id_prestamo)
    form = PrestamoForm(request.POST, instance=prestamo)
    if form.is_valid():
        form.save()
        return redirect('listado_prestamos')
    context = {
        'form': form,
        'prestamo': prestamo
    }
    return render(request, 'prestamo/editar.html', context)

def eliminar(request, id_prestamo):
    prestamo = get_object_or_404(Prestamo, id_prestamo=id_prestamo)
    prestamo.delete()
    return redirect('listado_prestamos')
