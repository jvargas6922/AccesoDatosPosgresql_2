from django.db import models
from apps.autor.models import Autor

# Create your models here.
class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=13)
    nombre = models.CharField(max_length=50)
    anio = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE, db_column='autor_id')

    # Se agrega las siguinetes lineas a mi modelos
    # (Aplica a todos los modelos del archivo ya que nos estamos conectando a una BD ya existente)!!!
    # managed = False para indicar que no se debe crear la tabla en la base de datos
    # db_table = 'libros' para indicar el nombre de la tabla en la base de datos
    class Meta:
        managed = False
        db_table = 'libros'
    
    def __str__(self):
        return self.nombre