from django.db import models

# Create your models here.

class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        # Se agrega las siguinetes lineas a mi modelos
        # (Aplica a todos los modelos del archivo ya que nos estamos conectando a una BD ya existente)!!!
        # managed = False para indicar que no se debe crear la tabla en la base de datos
        # db_table = 'autores' para indicar el nombre de la tabla en la base de datos
        verbose_name_plural = "Autores"
        managed = False
        db_table = 'autores'
    
    def __str__(self):
        return self.nombre_completo
    
class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=13)
    nombre = models.CharField(max_length=50)
    anio = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE, db_column='autor_id')

    class Meta:
        managed = False
        db_table = 'libros'
    
    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=80)
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=30)
    correo = models.EmailField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
    
    def __str__(self):
        return self.nombre_completo
    
class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True)
    fecha = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    libro_id = models.ForeignKey(Libro, on_delete=models.CASCADE, db_column='libro_id')
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='usuario_id')

    class Meta:
        managed = False
        db_table = 'prestamos'
    
    def __str__(self):
        return f"Prestamo de {self.libro_id.nombre} a {self.usuario_id.nombre_completo}"
    
