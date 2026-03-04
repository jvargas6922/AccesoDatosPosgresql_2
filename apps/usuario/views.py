from django.shortcuts import render,redirect, get_object_or_404
from .models import Usuario
from .forms import UserForm

# Create your views here.

def listado_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/listado.html', {'usuarios': usuarios})

def crear(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_usuarios')
    else:
        form = UserForm()
    return render(request, 'usuario/crear.html', {'form': form})

def editar(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    form = UserForm(instance=usuario)
    context = {
        'form': form,
        'usuario': usuario
    }
    return render(request, 'usuario/editar.html', context)

def actualizar(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    form = UserForm(request.POST, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('listado_usuarios')
    context = {
        'form': form,
        'usuario': usuario
    }
    return render(request, 'usuario/editar.html', context)

def eliminar(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listado_usuarios')
    context = {
        'usuario': usuario
    }
    return render(request, 'usuario/eliminar.html', context)
