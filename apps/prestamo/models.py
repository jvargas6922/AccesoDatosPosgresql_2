from django.db import models
from apps.libro.models import Libro
from apps.usuario.models import Usuario

# Create your models here.
class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True)
    fecha = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    libro_id = models.ForeignKey(Libro, on_delete=models.CASCADE, db_column='libro_id')
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='usuario_id')

    # Se agrega las siguinetes lineas a mi modelos
    # (Aplica a todos los modelos del archivo ya que nos estamos conectando a una BD ya existente)!!!
    # managed = False para indicar que no se debe crear la tabla en la base de datos
    # db_table = 'prestamos' para indicar el nombre de la tabla en la base de datos
    class Meta:
        managed = False
        db_table = 'prestamos'
    
    def __str__(self):
        return f"Prestamo de {self.libro_id.nombre} a {self.usuario_id.nombre_completo}"
