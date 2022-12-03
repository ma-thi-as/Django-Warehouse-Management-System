from django import forms

from .models import Inventario

class InventarioForm(forms.ModelForm):
    """Form definition for Inventario."""

    class Meta:
        """Meta definition for Inventarioform."""
        model = Inventario
        fields = ('producto','opcion','cantidad',)
        labels = {
            'producto': 'Producto',
            'opcion': 'Opcion a operar',
            'cantidad': 'Cantidad de productos',
        }
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-select'}),
            'opcion': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.Select(attrs={'class': 'form-select'}),


        }