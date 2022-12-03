from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Usuario

class FormularioLogin(AuthenticationForm):

    def __init__(self,  *args, **kwargs) :
        super(FormularioLogin,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['username'].widget.attrs['placeholder'] = 'Ingrese rut... '
        self.fields['password'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password'].widget.attrs['placeholder'] = 'Ingre su contraseña... '


class FormularioUsuario(forms.ModelForm):

    password1= forms.CharField(label = 'Contraseña',widget= forms.PasswordInput(
        attrs= {
            'class':'form-control form-control-lg',
            'placeholder':'Ingrese su contraseña...',
            'id':'password1',
            'required':'required',
        }
    ))
    password2= forms.CharField(label = 'Contraseña de confirmacion',widget= forms.PasswordInput(
            attrs= {
                'class':'form-control form-control-lg',
                'placeholder':'Ingrese nuevamente su contraseña...',
                'id':'password2',
                'required':'required',
            }
        ))
    

    class Meta:
        model = Usuario
        
        fields = ('rut','nombre','apellido','cargo',)
        lables ={
            'username':'Username',
            'nombre': 'Nombre Usuario',
            'apellido': 'Apellido  Usuario',
            'cargo':'cargo de usuario',
        }
        widgets = {
            'rut': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su rut de usuario...',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre...',

                }
            ),
            'apellido':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su apellido...',
                }
            ),
            
            'cargo': forms.Select(
                attrs={
                    'class':'form-select',
                }
            ),
        }

    def clean_password2(self):
        """
        Validacion de contraseña
        Metodo que valida qye ambas contraseñas sean iguales, antes de ser encriptadas y guardadas en la bd, retorna la contraseña valida
        Exepciones:
        - ValidationError -- cuando las contraseñas no son iguales muestra un mensaje de error
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden!')

        return password2
    
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

        

    def save(self, commit = True):
        user = super().save(commit= False)#Guardamos la instancia de la informacion.
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user