from django import forms 

from .models import Proveedor
class ProveedorForm(forms.ModelForm):
    """Form definition for Proveedor."""

    class Meta:
        """Meta definition for Proveedorform."""

        model = Proveedor
        fields = ('nombre','apellido','email','rut','detalle',)
        lables ={
            'nombre': 'Nombre del proveedor',
            'apellido': 'Apellido  del proveedor',
            'rut':'Rut del proveedor',
            'email': 'Email del proveedor',
            'detalle': 'Detalle del proveedor',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre del proveedor'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Apellido del proveedor'}),
            'rut': forms.TextInput(attrs={'class': 'form-control','placeholder':'Rut del proveedor'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Correo del proveedor'}),  
            'detalle': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Detalle productos proveeidos por el proveedor'})
        }

    def clean_rut(self):
        """Validacion campo rut."""
        rut = self.cleaned_data.get('rut')
        rut_numerico = rut.isdigit()

        if not rut_numerico:
            try:
                if rut.index('K') != 8:
                    raise forms.ValidationError('Solo se permite caracteres al final')
            except:
                    raise forms.ValidationError('Solo se permiten letras "K" mayuscúlas al final del rut')
        return rut

        
class ProveedorAdminForm(forms.ModelForm):
    """Form definition for Proveedor."""

    class Meta:
        """Meta definition for Proveedorform."""

        model = Proveedor
        fields = ('nombre','apellido','email','rut','detalle','estado',)
        lables ={
            'nombre': 'Nombre del proveedor',
            'apellido': 'Apellido  del proveedor',
            'rut':'Rut del proveedor',
            'email': 'Email del proveedor',
            'detalle': 'Detalle del proveedor',
            'estado': 'Estado del proveedor',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre del proveedor'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Apellido del proveedor'}),
            'rut': forms.TextInput(attrs={'class': 'form-control','placeholder':'Rut del proveedor'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Correo del proveedor'}),  
            'detalle': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Detalle productos proveeidos por el proveedor'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input','placeholder': 'Estado del proveedor'})

        }

    def clean_rut(self):
        """Validacion campo rut."""
        rut = self.cleaned_data.get('rut')
        rut_numerico = rut.isdigit()

        if not rut_numerico:
            try:
                if rut.index('K') != 8:
                    raise forms.ValidationError('Solo se permite caracteres al final')
            except:
                    raise forms.ValidationError('Solo se permiten letras "K" mayuscúlas al final del rut')
        return rut

        