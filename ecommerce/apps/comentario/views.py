from django.shortcuts import render, HttpResponseRedirect
from .models import Comentario
from productos.models import Producto
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

# Create your views here.
def Comentar(request,pk):
    pro = Producto.objects.get(pk = pk)
    usuario = request.user
    com = request.POST.get('comentario',None)

    Comentario.objects.create(texto = com, producto = pro, usuario = usuario)

    return HttpResponseRedirect(reverse_lazy('productos:path_detalle_producto', kwargs={'pk':pk}))

class Eliminar(DeleteView):
    model = Comentario
    def get_success_url(self):
        return reverse_lazy('productos:path_detalle_producto', kwargs={'pk':self.object.producto.pk})