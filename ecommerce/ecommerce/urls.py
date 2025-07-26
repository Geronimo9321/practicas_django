from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #1° parametro es la url
    #2° parametro es la vista que se ejecuta
    #3° parametro es el nombre de este path
    #4° repetir los pasos para agregar mas rutas, referencia la linea 12
    #path('categoria', views.Categoria, name = 'path_categoria'),
    path('', views.Home, name = 'path_home'),

    #INCLUIR LAS APP
    path('Productos/', include('productos.urls')),
    path('Genericos/', include('genericos.urls')),
    path('Usuario/', include('usuario.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
