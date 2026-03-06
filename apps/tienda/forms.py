from django import forms
from .models import Categoria, Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre_categoria']
        labels ={
            'nombre_categoria': 'Nombre de la categoría',
        }
        widgets = {
            'nombre_categoria': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProductoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(deleted_at__isnull=True)
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'precio', 'categoria']
        labels = {
            'nombre_producto': 'Nombre del producto',
            'precio': 'Precio',
            'categoria': 'Categoría',
        }
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }