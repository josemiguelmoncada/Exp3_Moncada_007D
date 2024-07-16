from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto, Tipo_producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'ingredientes', 'tipo', 'precio', 'imagen', 'stock']
        labels = {
            'nombre': 'Nombre Producto',
            'descripcion': 'Descripción',
            'ingredientes': 'Ingredientes',
            'tipo': 'Tipo Producto',
            'precio': 'Precio',
            'imagen': 'Imagen',
            'stock': 'Stock'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre del producto',
                    'id': 'nombre'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese descripción del producto',
                    'id': 'descripcion'
                }
            ),
            'ingredientes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese descripción del producto',
                    'id': 'descripcion'
                }
            ),
            'tipo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione tipo de producto',
                    'id': 'tipo'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese precio del producto',
                    'id': 'precio'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen'
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese stock del producto',
                    'id': 'stock'
                }
            )
        }

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo_producto
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre Tipo'
            }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre de Tipo',
                    'id': 'nombre'
                }
            )
            }


class RegistroUsuarioForm(UserCreationForm):
    first_name  = forms.CharField(
        max_length=30,
        required=True,
        label="Nombre (*)",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su nombre',
            'id': 'nom',
            'name': 'nom'
        })
    )
    email = forms.EmailField(
        max_length=254,
        help_text='Correo electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su correo electrónico',
            'id': 'correo',
            'name': 'correo'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Usuario (*)',
            'password1': 'Ingrese su contraseña (*)',
            'password2': 'Verifique su contraseña (*)',
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Usuario',
                    'id': 'usu',
                    'name': 'usu'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña',
            'id': 'pass1',
            'name': 'pass1'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Verifique su contraseña',
            'id': 'pass2',
            'name': 'pass2'
        })
        
class EmailForm(forms.Form):
    email = forms.EmailField(label='Nuevo correo electrónico', max_length=254)

class BuscarProductoForm(forms.Form):
    query = forms.CharField(label="Buscar", max_length=100)
