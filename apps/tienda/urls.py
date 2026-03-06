from django.urls import path
from . import views

urlpatterns = [
    # rutas categorias
    path('categorias/', views.listado_categorias, name='listado_categorias'),
    path('categoria/crear/', views.crear_categoria, name='crear_categoria'),
    path('categoria/editar/<int:id_categoria>/', views.editar_categoria, name='editar_categoria'),
    path('categoria/actualizar/<int:id_categoria>/', views.actualizar_categoria, name='actualizar_categoria'),
    path('categoria/eliminar/<int:id_categoria>/', views.eliminar_categoria, name='eliminar_categoria'),
    # Rutas productos por categoria
    path('categorias_tienda/', views.listado_categoria_tienda, name='listado_categoria_tienda'),
    path('categoria/<int:id_categoria>/productos/', views.productos_por_categoria, name='productos_por_categoria'),
    # Rutas productos
    path('productos/', views.listado_productos, name='listado_productos'),
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    path('producto/editar/<int:id_producto>/', views.editar_producto, name='editar_producto'),
]