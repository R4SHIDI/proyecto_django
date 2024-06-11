from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm

# Create your views here.






def index(request):
     return render(request, 'paginas/index.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')

def login(request):
    return render(request, 'paginas/login.html')

def registro (request):
    return render(request, 'paginas/registro.html')

def tienda (request):
    return render(request, 'paginas/tienda.html')

def crud(request):
    Productos = Producto.objects.all()
    return render(request, 'crud/vista.html', {'productos':Productos})


def crear(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('crud')
    return render(request, 'crud/crear.html', {'formulario':formulario})

def editar(request, id):
    producto = Producto.objects.get(id=id)
    formulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('crud')
    return render(request, 'crud/editar.html', {'formulario':formulario})
def eliminar(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('crud')

def vista(request):
    return render(request, 'crud/vista.html')



