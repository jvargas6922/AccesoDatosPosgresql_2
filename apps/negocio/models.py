from django.db import models

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    articulo = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    class Meta:
        db_table = 'compras'
    
    def __str__(self):
        return f"Compra realizada el {self.articulo}"