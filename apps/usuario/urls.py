from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_usuarios, name='listado_usuarios'),
    path('crear/', views.crear, name='crear_usuario'),
    path('editar/<int:id_usuario>/', views.editar, name='editar_usuario'),
    path('actualizar/<int:id_usuario>/', views.actualizar, name='actualizar_usuario'),
    path('eliminar/<int:id_usuario>/', views.eliminar, name='eliminar_usuario'),
]