from django.urls import path

from . import views

app_name = "productos"

urlpatterns = [
    path('Listar', views.Listar_Productos, name = 'path_listar_productos'), #URL PARA VER LOS PRODUCTOS
    #path('Detalle/<int:pk>', views.Detalle_Productos, name = 'path_detalle_productos'), #URL PARA VER LOS DETALLES DE PRODUCTOS
    path('Detalle/<int:pk>', views.Detalle_Productos_Clase.as_view(), name = 'path_detalle_productos'),#URL PARA VER LOS DETALLES DE PRODUCTOS CON AS_VIEW()
    path('Crear/', views.Crear_Producto.as_view(), name= 'path_crear_productos'),
    path('Modificar/<int:pk>', views.Modificar_Producto.as_view(), name= 'path_modificar_productos'),
    path('Eliminar/<int:pk>', views.Borrar_Producto.as_view(), name= 'path_borrar_productos'),

    #FILTRO POR RUBRO
    path('Filtrados/<int:pk>', views.Filtrar_Rubro, name='path_filtro_rubros'), #porque no reconoce esto
]
