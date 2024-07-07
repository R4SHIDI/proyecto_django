from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import Contacto, Producto, Clientesss, Marca, Factura
from .forms import ProductoForm, CustomUserCreationForm, ClientesForm, MarcaForm, FacturaForm
from django.contrib.auth import authenticate, login
from django.contrib import messages





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

def logueo(request):
    return render(request, 'paginas/logueo.html')

def registratee (request):
    return render(request, 'paginas/registratee.html')

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

##registro de usuario de auth django con form entregado por el framework validaciones
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request,"te has registrado correctamente")
            #redirigo a la vista
            return redirect(to='vista')
            print("Redirigiendo a ")
            data["form"] = formulario

    return render(request, 'registration/registro.html', data)



#cliente crud LA VARIABLE {'clientes': clientes})  PUEDE ESTAR MALA
def clientes(request):
    clientes = Clientesss.objects.all()
    return render(request, 'clientes/inicio.html', {'clientes': clientes}) 

def crear_cliente(request):
    formulario = ClientesForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        #recepcionar los datos 
        return redirect('clientes')
    return render(request, 'clientes/crear_cliente.html', {'formulario': formulario})


def editar_clientes(request, id):
    cliente = Clientesss.objects.get(id=id)
    formulario = ClientesForm(request.POST or None, request.FILES or None, instance=cliente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('clientes')
    return render(request, 'clientes/editar_cliente.html', {'formulario': formulario})

def eliminar_clientes(request, id):
    cliente = Clientesss.objects.get(id=id)
    cliente.delete()
    return redirect('clientes')

    #######

#CRUD MARCA  borrar todo si no sirve 
def marca(request):
    marcas = Marca.objects.all()  # Recuperar todas las marcas desde la base de datos
    return render(request, 'marca/principal.html', {'marcas': marcas})  # Pasar 'marcas' en lugar de 'marca'

def crear_marca(request):
    formulario = MarcaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        #recepcionar los datos 
        return redirect('marca')
    return render(request, 'marca/crear_marca.html', {'formulario': formulario})


def editar_marca(request, id):
    marca = Marca.objects.get(id=id)
    formulario = MarcaForm(request.POST or None, request.FILES or None, instance=marca)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('marca')
    return render(request, 'marca/editar_marca.html', {'formulario': formulario})

def eliminar_marca(request, id):
    marca = Marca.objects.get(id=id)
    marca.delete()
    return redirect('marca')



#########CRUD FACTURAS @@@@@@@2

def factura(request):
    facturas = Factura.objects.all()
    return render(request, 'factura/visual.html', {'facturas': facturas}) 

def crear_factura(request):
    formulario = FacturaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        #recepcionar los datos 
        return redirect('factura')
    return render(request, 'factura/crear_factura.html', {'formulario': formulario})


def editar_factura(request, id):
    factura = Factura.objects.get(id=id)
    formulario = FacturaForm(request.POST or None, request.FILES or None, instance=factura)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('factura')
    return render(request, 'factura/editar_factura.html', {'formulario': formulario})

def eliminar_factura(request, id):
    factura = Factura.objects.get(id=id)
    factura.delete()
    return redirect('factura')