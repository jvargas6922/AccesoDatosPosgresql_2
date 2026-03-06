from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Producto
from .forms import CategoriaForm, ProductoForm
# Create your views here.

def listado_categorias(request):
    # categoria = 1
    # restaurar_categoria(id_categoria=categoria)  # Ejemplo de restauración de una categoría con ID 1
        categorias = Categoria.objects.filter(deleted_at__isnull=True)
        return render(request, 'tienda/categoria/listado.html', {'categorias': categorias})

def listado_categoria_tienda(request):
    categorias = Categoria.objects.filter(deleted_at__isnull=True)
    return render(request, 'tienda/categoria/listado_categoria.html', {'categorias': categorias})

def productos_por_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria, deleted_at__isnull=True)
    productos = Producto.objects.filter(categoria_id=id_categoria, deleted_at__isnull=True)
    context = {
        'categoria': categoria,
        'productos': productos,
    }
    return render(request, 'tienda/categoria/productos_por_categoria.html', context)

def crear_categoria(request):
    if request.method == 'POST':
        print(request.POST)
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'tienda/categoria/crear.html', {'form': form})

def editar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    form = CategoriaForm(instance=categoria)
    context ={
        'form': form,
        'categoria': categoria,
    }
    return render(request, 'tienda/categoria/editar.html', context)

def actualizar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listado_categorias')
    else:
        form = CategoriaForm(instance=categoria)
        context ={
            'form': form,
            'categoria': categoria,
        }
    return render(request, 'tienda/categoria/editar.html', context)

def eliminar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    categoria.delete()
    return redirect('listado_categorias')

def restaurar_categoria(id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    categoria.restore()
    return redirect('listado_categorias')


def listado_productos(request):
    productos = Producto.objects.filter(deleted_at__isnull=True, categoria__deleted_at__isnull=True)
    print(productos)
    return render(request, 'tienda/producto/listado.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        print(request.POST)
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_productos')
    else:
        form = ProductoForm()
        context = {
            'form': form,
        }
    return render(request, 'tienda/producto/crear.html', context)

def editar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    form = ProductoForm(instance=producto)
    context ={
        'form': form,
        # 'producto': producto,
    }
    return render(request, 'tienda/producto/editar.html', context)


    
