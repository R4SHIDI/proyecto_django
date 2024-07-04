from django import forms
from .models import Producto, Venta


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

# BORRAR SI NO SIRVE###

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'  # O puedes especificar los campos que quieres incluir en el formulario