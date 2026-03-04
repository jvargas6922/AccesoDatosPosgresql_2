from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_prestamos, name='listado_prestamos'),
    path('crear/', views.crear, name='crear_prestamo'),
    path('editar/<int:id_prestamo>/', views.editar, name='editar_prestamo'),
    path('actualizar/<int:id_prestamo>/', views.actualizar, name='actualizar_prestamo'),
    path('eliminar/<int:id_prestamo>/', views.eliminar, name='eliminar_prestamo'),
]