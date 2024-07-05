
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecommerce.urls')),
    path('accounts/', include('django.contrib.auth.urls')),   #agregue esto para habilitar el login y logout    
    
 
      
]
