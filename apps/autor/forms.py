from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre_completo', 'nacionalidad']
        labels = {
            'nombre_completo': 'Nombre Completo',
            'nacionalidad': 'Nacionalidad',
        }
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
        }