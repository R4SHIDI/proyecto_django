from django import forms
from .models import Producto, Clientesss, Marca
from django.contrib.auth.forms import UserCreationForm


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


#FORMS DE CRUD CLIENTES

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientesss
        fields = '__all__'


##marca form@@@@

####crud marca #marca
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass