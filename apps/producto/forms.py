from cProfile import label
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

from .models import Producto, Categoria, Unidad_Medida

class ProductoForm(forms.ModelForm):
    """Form definition for Producto."""

    class Meta:
        """Meta definition for Productoform."""

        model = Producto
        fields = ('nombre', 'precio', 'detalle',  'unidad', 'categoria',)
        labels ={
            'nombre': 'Nombre',
            'precio': 'Precio',
            'detalle': 'Detalle',
            'unidad': 'Unidad',
            'categoria': 'Categoria',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese el nombre del producto'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder ': 'Ingrese el precio del producto'}),
            'detalle': forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Detalles del producto'}),
            'unidad': forms.Select(attrs={'class': 'form-select', 'placeholder' : 'Ingrese la unidad de medida del producto'}),
            'categoria': forms.Select(attrs={'class': 'form-select', 'placeholder' : 'Ingrese la categorias del producto'}),
        }

class CategoriaForm(forms.ModelForm):
    """Form definition for Categoria."""

    class Meta:
        """Meta definition for Categoriaform."""

        model = Categoria
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'estado': 'Estado',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Ingrese categoria del producto'}),
            'estado':forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }

class Unidad_MedidaForm(forms.ModelForm):
    """Form definition for Unidad_Medida."""

    class Meta:
        """Meta definition for Unidad_Medidaform."""

        model = Unidad_Medida
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese unidad de medida'}),
            'estado':forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }

