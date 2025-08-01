from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Producto
from .forms import FormularioCrearProducto, FormularioModificarProducto
from genericos.models import Rubro

# Create your views here.
# PARA LISTAR LOS PRODUCTOS USO ORM.
# __gt significa > (mayor)
# __gte significa >= (mayor igual)
# __lt significa < (menor)
# __lte significa <= (menor igual)

#DECORADOR PARA UNA VISTA BASADA EN FUNCIONES QUE CONTROLA SI EL USUARIO ESTA LOGUEADO
from django.contrib.auth.decorators import login_required

#MIXINS PARA UNA VISTA BASADA EN CLASES QUE CONTROLA SI EL USUARIO ESTA LOGUEADO
from django.contrib.auth.mixins import LoginRequiredMixin 

#DECORADOR PARA UNA VISTA BASADA EN FUNCIONES PARA CONTROLAR SI EL USUARIO ES ESTAFF
from django.contrib.admin.views.decorators import staff_member_required

#MIXINS PARA UNA VISTA BASADA EN CLASES PARA CONTROLAR EL TIPO DE USUARIO (LO USAMOS PARA VER SI ES ESTAFF) 
from django.contrib.auth.mixins import UserPassesTestMixin

@login_required
@staff_member_required
def Listar_Productos(request): #Esto es una VISTA BASADA EN FUNCIONES

    valor_a_ordenar = request.GET.get('orden', None)#Esta variable devuelve un orden desc-asc o simplemente
    if valor_a_ordenar:
        #Significa que la orden si vino
        if valor_a_ordenar == 'asc':
            solo_stock = Producto.objects.filter(stock__gt = 0).order_by('precio')
        else:
            solo_stock = Producto.objects.filter(stock__gt = 0).order_by('-precio')
    else:
        solo_stock = Producto.objects.filter(stock__gt = 0) #Es igual que hacer SELECT * FROM Producto where stock > 0

    #todos = Producto.objects.all() #Reemplazo las sentencias SQL por el ORM para traer los productos.
    todos_rubros = Rubro.objects.all()
    return render(request, 'productos/listar.html', {'productos':solo_stock, 'rubros':todos_rubros})

def Detalle_Productos(request,pk):

    p = Producto.objects.get(pk = pk)
    return render(request, 'productos/detalle.html', {'productos':p})

class Detalle_Productos_Clase(DetailView): #Esto es una VISTA BASADA EN CLASES
    template = 'productos/detalle.html'
    model = Producto
    context_object_name = 'productos'

class Crear_Producto(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = Producto
    template_name = 'productos/crear.html'
    form_class = FormularioCrearProducto
    success_url = reverse_lazy('productos:path_listar_productos')

    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return False

class Modificar_Producto(UpdateView):
    model = Producto
    template_name = 'productos/modificar.html'
    form_class = FormularioModificarProducto
    success_url = reverse_lazy('productos:path_listar_productos')

class Borrar_Producto(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos:path_listar_productos')

def Filtrar_Rubro(request, pk):
    rubro_filtrado = Rubro.objects.get(pk = pk)
    productos_filtrados = Producto.objects.filter(rubro=rubro_filtrado) #Solución  

    return render(request, 'productos/filtrados.html', {'productos':productos_filtrados, 'nombre_rubro':rubro_filtrado.nombre})