from django import forms
from .models import Producto, Usuario, ContactMessage

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'foto']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'password', 'telefono', 'direccion']
        widgets = {
            'password': forms.PasswordInput(),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['nombre', 'email', 'mensaje']
