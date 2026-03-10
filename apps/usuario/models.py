from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=80)
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=30)
    correo = models.EmailField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Se agrega las siguinetes lineas a mi modelos
    # (Aplica a todos los modelos del archivo ya que nos estamos conectando a una BD ya existente)!!!
    # managed = False para indicar que no se debe crear la tabla en la base de datos
    # db_table = 'usuarios' para indicar el nombre de la tabla en la base de datos
    class Meta:
        managed = False
        db_table = 'usuarios'

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()
    
    def __str__(self):
        return self.nombre_completo