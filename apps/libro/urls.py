from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_libros, name='listado_libros'),
    path('crear/', views.crear, name='crear_libro'),
    path('editar/<int:id_libro>/', views.editar, name='editar_libro'),
    path('actualizar/<int:id_libro>/', views.actualizar, name='actualizar_libro'),
    path('eliminar/<int:id_libro>/', views.eliminar, name='eliminar_libro'),
]