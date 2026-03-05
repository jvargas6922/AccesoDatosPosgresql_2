from django import forms
from .models import Prestamo
from apps.libro.models import Libro
from apps.usuario.models import Usuario

class PrestamoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        libros = kwargs.pop('libros', None) # Extraemos los libros del kwargs(kwargs es un diccionario que contiene los argumentos pasados a la función)
        usuarios = kwargs.pop('usuarios', None) # Extraemos los usuarios del kwargs(kwargs es un diccionario que contiene los argumentos pasados a la función)
        super().__init__(*args, **kwargs)
        self.fields['libro_id'].queryset = libros if libros is not None else Libro.objects.all() # Si se proporcionan libros, se asignan al queryset del campo libro_id; de lo contrario, se asignan todos los libros disponibles.
        self.fields['usuario_id'].queryset = usuarios if usuarios is not None else Usuario.objects.all() # Si se proporcionan usuarios, se asignan al queryset del campo usuario_id; de lo contrario, se asignan todos los usuarios disponibles.

    class Meta:
        model = Prestamo
        fields = ['fecha', 'libro_id', 'usuario_id']
        labels = {
            'fecha': 'Fecha del Préstamo',
            'libro_id': 'Libro',
            'usuario_id': 'Usuario',
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'libro_id': forms.Select(attrs={'class': 'form-control'}),
            'usuario_id': forms.Select(attrs={'class': 'form-control'}),
        }