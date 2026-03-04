from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_autores, name='listado_autores'),
    path('crear/', views.crear, name='crear_autor'),
    path('editar/<int:id_autor>/', views.editar, name='editar_autor'),
    path('actualizar/<int:id_autor>/', views.actualizar, name='actualizar_autor'),
    path('eliminar/<int:id_autor>/', views.eliminar, name='eliminar_autor'),
]