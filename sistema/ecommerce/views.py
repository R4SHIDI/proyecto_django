from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import Contacto, Producto, Venta
from .forms import ProductoForm

##ventas###
from .forms import VentaForm


# Create your views here.






def index(request):
     return render(request, 'paginas/index.html')

def contacto(request):
    context={}
    return render(request, 'paginas/contacto.html', context)

def registrar(request):
 
    nombre = request.POST['nombre']
    email  = request.POST['email']
    mensaje = request.POST['mensaje']

    contacto = Contacto.objects.create(nombre=nombre, email=email, Mensaje=mensaje)

    contacto = Contacto.objects.all()
    context = {'contacto': contacto}
    return render(request, 'paginas/index.html', context)

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

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




######nuevo vistas para la ventas######

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'crud/lista_ventas.html', {'ventas': ventas})

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = VentaForm()
    return render(request, 'crud/crear_venta.html', {'form': form})

def ver_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    return render(request, 'crud/ver_venta.html', {'venta': venta})

def editar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'crud/editar_venta.html', {'form': form})

def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('lista_ventas')
    return render(request, 'crud/eliminar_venta.html', {'venta': venta})