from django import forms 
from .models import Producto

class FormularioCrearProducto(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('nombre', 'stock', 'precio', 'imagen', 'rubro')

class FormularioModificarProducto(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('nombre', 'stock', 'precio', 'rubro')