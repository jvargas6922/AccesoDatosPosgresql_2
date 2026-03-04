from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['isbn', 'nombre', 'anio', 'autor_id']
        labels = {
            'isbn': 'ISBN',
            'nombre': 'Nombre',
            'anio': 'Año',
            'autor_id': 'Autor',
        }
        widgets = {
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
            'autor_id': forms.Select(attrs={'class': 'form-control'}),
        }