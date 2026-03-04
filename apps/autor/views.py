from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor
from .forms import AutorForm

# Create your views here.
def listado_autores(request):
    autores = Autor.objects.all()
    return render(request, 'autor/listado.html', {'autores': autores})

def crear(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_autores')
    else:
        form = AutorForm()
    return render(request, 'autor/crear.html', {'form': form})

def editar(request, id_autor):
    autor = get_object_or_404(Autor, id_autor=id_autor)
    form = AutorForm(instance=autor)
    context = {
        'form': form,
        'autor': autor
    }
    return render(request, 'autor/editar.html', context)

def actualizar(request, id_autor):
    autor = get_object_or_404(Autor, id_autor=id_autor)
    form = AutorForm(request.POST, instance=autor)
    if form.is_valid():
        form.save()
        return redirect('listado_autores')
    context = {
        'form': form,
        'autor': autor
    }
    return render(request, 'autor/editar.html', context)

def eliminar(request, id_autor):
    autor = Autor.objects.get(id_autor=id_autor)
    autor.delete()
    return redirect('listado_autores')