from django.db import models

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
    

# nuevoooo ventas no servir, (BORRAR)







    