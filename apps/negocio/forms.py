from django import forms
from .models import Compra, Cliente

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['valor', 'articulo']
        labels = {
            'valor': 'Valor de la compra',
            'articulo': 'Artículo comprado',
        }
        widgets = {
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'articulo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono']
        labels = {
            'nombre': 'Nombre del cliente',
            'apellido': 'Apellido del cliente',
            'email': 'Correo electrónico del cliente',
            'telefono': 'Número de teléfono del cliente',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }