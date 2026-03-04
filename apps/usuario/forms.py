from django import forms
from .models import Usuario

class UserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_completo', 'rut', 'telefono', 'correo']
        labels = {
            'nombre_completo': 'Nombre Completo',
            'rut': 'RUT',
            'telefono': 'Teléfono',
            'correo': 'Correo Electrónico',
        }
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }
