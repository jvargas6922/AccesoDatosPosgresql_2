from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor
from .forms import AutorForm

# Create your views here.
def listado_autores(request):
    # Esta consulta me trae todos los registros indiferentemente de su estado, es decir, si están eliminados o no.
    # autores = Autor.objects.all()

    # Esta consulta me debe devolver los registros que no cumplen la condición, es decir, los autores cuya nacionalidad no es "Ingles".
    autores_e = Autor.objects.exclude(nacionalidad="Ingles")
    print(autores_e)


    # Esta consulta me trae solo los registros que no están eliminados (deleted_at es null).
    autores = Autor.objects.filter(deleted_at__isnull=True)
    # autor_eliminado = Autor.objects.filter(deleted_at__isnull=False).first()  # Obtener el primer autor eliminado (si existe)
    # print(autor_eliminado.id_autor)

    # restaurar_registro(id_autor=autor_eliminado.id_autor)
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

def restaurar_registro(id_autor):
    autor = get_object_or_404(Autor, id_autor=id_autor)
    autor.restore()
    return redirect('listado_autores')