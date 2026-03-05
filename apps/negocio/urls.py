from django.urls import path
from .import views

urlpatterns = [
    path('compras/', views.listado_compras, name='listado_compras'),
    path('compras/crear/', views.crear_compra, name='crear_compra'),
    path('compras/editar/<int:id_compra>/', views.editar_compra, name='editar_compra'),
    path('compras/actualizar/<int:id_compra>/', views.actualizar_compra, name='actualizar_compra'),
    path('compras/eliminar/<int:id_compra>/', views.eliminar_compra, name='eliminar_compra'),
]