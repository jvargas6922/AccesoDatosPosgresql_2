from django.db import models

# Create your models here.

class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Se agrega las siguinetes lineas a mi modelos
    # (Aplica a todos los modelos del archivo ya que nos estamos conectando a una BD ya existente)!!!
    # managed = False para indicar que no se debe crear la tabla en la base de datos
    # db_table = 'autores' para indicar el nombre de la tabla en la base de datos
    class Meta:
        verbose_name_plural = "Autores"
        managed = False
        db_table = 'autores'
    
    def __str__(self):
        return self.nombre_completo
