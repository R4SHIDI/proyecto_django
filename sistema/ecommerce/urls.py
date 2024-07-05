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
    
  


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
