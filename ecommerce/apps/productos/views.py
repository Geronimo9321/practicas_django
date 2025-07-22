from django.shortcuts import render
from .models import Producto
from django.views.generic.detail import DetailView

# Create your views here.
# PARA LISTAR LOS PRODUCTOS USO ORM.
# __gt significa > (mayor)
# __gte significa >= (mayor igual)
# __lt significa < (menor)
# __lte significa <= (menor igual)


def Listar_Productos(request): #Esto es una VISTA BASADA EN FUNCIONES

    todos = Producto.objects.all() #Reemplazo las sentencias SQL por el ORM para traer los productos.
    solo_stock = Producto.objects.filter(stock__gt = 0) #Es igual que hacer SELECT * FROM Producto where stock > 0
    return render(request, 'productos/listar.html', {'productos':solo_stock})

def Detalle_Productos(request,pk):

    p = Producto.objects.get(pk = pk)
    return render(request, 'productos/detalle.html', {'productos':p})

class Detalle_Productos_Clase(DetailView): #Esto es una VISTA BASADA EN CLASES
    template = 'productos/detalle.html'
    model = Producto
    context_object_name = 'productos'