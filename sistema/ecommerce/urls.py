from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('registrar', views.registrar, name='registrar'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('crud', views.crud, name='crud'),
    path('logueo', views.logueo, name='logueo'),
    path('tienda', views.tienda, name='tienda'),
    path('registratee', views.registratee, name='registratee'),
    path('crud/crear', views.crear, name='crear'),
    path('crud/editar', views.editar, name='editar'),
    path('vista/', views.vista, name='vista'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('productos/editar/<int:id>', views.editar, name='editar'),
    path('registro/', views.registro, name='registro'),
    #cliente crud
    path('clientes',views.clientes, name='clientes'),
    path('clientes/crear_cliente',views.crear_cliente, name='crear_cliente'),
    path('clientes/editar_clientes',views.editar_clientes, name='editar_clientes'),
    path('eliminar_clientes/<int:id>', views.eliminar_clientes, name='eliminar_clientes'),
    path('clientes/editar_clientes/<int:id>/', views.editar_clientes, name='editar_clientes'),

#@@@@@@@@@@@@@@@URLS DE CRUD MARCA@@@@@@@@################
    path('marca',views.marca, name='marca'),
    path('marca/crear_marca',views.crear_marca, name='crear_marca'),
    path('marca/editar_marca',views.editar_marca, name='editar_marca'),
    path('eliminar_marca/<int:id>', views.eliminar_marca, name='eliminar_marca'),
    path('marca/editar_marca/<int:id>/', views.editar_marca, name='editar_marca'),

#$$$$$URLS DE FACTURA@@@@@@@
    path('factura',views.factura, name='factura'),
    path('factura/crear_factura',views.crear_factura, name='crear_factura'),
    path('factura/editar_factura',views.editar_factura, name='editar_factura'),
    path('eliminar_factura/<int:id>', views.eliminar_factura, name='eliminar_factura'),
    path('factura/editar_factura/<int:id>/', views.editar_factura, name='editar_factura'),

#@@@@crud venta urls



    path('venta',views.venta, name='venta'),
    path('venta/crear_venta',views.crear_venta, name='crear_venta'),
    path('venta/editar_venta',views.editar_venta, name='editar_venta'),
    path('eliminar_venta/<int:id>', views.eliminar_venta, name='eliminar_venta'),
    path('venta/editar_venta/<int:id>/', views.editar_venta, name='editar_venta'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
