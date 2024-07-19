from django.db import models
from django.contrib.auth.decorators import login_required

# Create your models here.

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100, verbose_name='Marca')
    imagen = models.ImageField(upload_to='Imagenes/',verbose_name="Imagen", null=True)
    descripción = models.TextField(verbose_name="Descripción", null=True)

 


    def __str__(self):
        fila = "Marca: " + self.marca + " - " + "Descripción: " + self.descripción
        return fila
    


    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

     
class Contacto(models.Model):
    id_genero = models.AutoField(db_column='idContacto', primary_key=True)
    nombre    = models.CharField(max_length=20)
    email     = models.CharField(max_length=200)
    Mensaje    = models.CharField(max_length=200)

    def __str__(self):
         return str(self.nombre)+" "+str(self.email)
    
    

    #modelo clientes#


class Clientesss(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    apellido = models.CharField(max_length=20, verbose_name='Apellido')
    direccion = models.TextField(max_length=225, verbose_name='Direccion')


    def __str__(self):   
     fila = "Nombre: " + self.nombre + "- " + "Apellido:"  + self.apellido
     return self.nombre+" "+self.apellido+" "+self.direccion

   
##models de marca###

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=20, verbose_name='Marca')
    categoria = models.CharField(max_length=20, verbose_name='Categoria')
    precio = models.TextField(max_length=225, verbose_name='Precio')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True, blank=True) 
    
    def __str__(self):
        fila = "Marca: " + self.marca + " - " + "Categoria: " + self.categoria+" "+ self.precio + " - " + " Precio "
        return fila 
    


    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete() # Nuevo campo de imagen     





######CRUD FACTURAS 

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=250, verbose_name='Fecha')
    nombre = models.CharField(max_length=250, verbose_name='Nombre')
    monto = models.CharField(max_length=250, verbose_name='Monto')
     
    def __str__(self):
        fila = "Fecha: " + self.fecha + " - " + "Nombre: " + self.rut+" "+ self.precio + " - " + " Precio "
        return fila 
    



######CRUD FACTURAS 

class Ventas(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=250, verbose_name='Producto')
    cantidad = models.CharField(max_length=250, verbose_name='Cantidad')
     
    def __str__(self):
        fila = "Producto: " + self.producto+" "+ self.cantidad + " - " + " Cantidad "
        return fila 