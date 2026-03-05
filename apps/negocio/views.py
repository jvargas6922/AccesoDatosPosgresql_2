from django.shortcuts import render, redirect, get_object_or_404
from .models import Compra
from .forms import CompraForm

# Create your views here.

def listado_compras(request):
    compras = Compra.objects.all()
    return render(request, 'compra/listado.html', {'compras': compras})

def crear_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_compras')
    else:
        form = CompraForm()
    return render(request, 'compra/crear.html', {'form': form})

def editar_compra(request, id_compra):
    compra = get_object_or_404(Compra, id_compra=id_compra)
    print(compra)
    form = CompraForm(instance=compra)
    context = {
        'form': form,
        'compra': compra
    }
    return render(request, 'compra/editar.html', context)

def actualizar_compra(request, id_compra):
    compra = get_object_or_404(Compra, id_compra=id_compra)
    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('listado_compras')
    else:
        form = CompraForm(instance=compra)
    return render(request, 'compra/editar.html', {'form': form, 'compra': compra})

def eliminar_compra(request, id_compra):
    compra = get_object_or_404(Compra, id_compra=id_compra)
    compra.delete()
    return redirect('listado_compras')
