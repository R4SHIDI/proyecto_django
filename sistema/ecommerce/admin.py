from django.contrib import admin
from. models import Producto, Contacto, Clientesss, Marca, Factura
# Register your models here.
admin.site.register(Producto)
admin.site.register(Clientesss)
admin.site.register(Marca)
admin.site.register(Factura)



#GENERO CLASE PARA DESPLIGUE DE LAS TABLAS DE CONTACTOS

class ContactoAdmin(admin.ModelAdmin):
 list_display = ('nombre', 'email', 'Mensaje' )

#Registro el modelo y la clase
admin.site.register(Contacto, ContactoAdmin)


#modelo de clase ventas 



