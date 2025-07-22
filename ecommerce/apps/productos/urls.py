from django.urls import path

from . import views

app_name = "productos"

urlpatterns = [
    path('Listar', views.Listar_Productos, name = 'path_listar_productos'), #URL PARA VER LOS PRODUCTOS
    #path('Detalle/<int:pk>', views.Detalle_Productos, name = 'path_detalle_productos'), #URL PARA VER LOS DETALLES DE PRODUCTOS
    path('Detalle/<int:pk>', views.Detalle_Productos_Clase.as_view(), name = 'path_detalle_productos'),
]
