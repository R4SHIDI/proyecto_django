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