from django import forms
from .models import Compra

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