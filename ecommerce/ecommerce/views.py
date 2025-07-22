from django.shortcuts import render
#agregar una funcion para cada archivo.html

def Home(request):
    return render(request, 'home.html')

#def Categoria(request):
    #return render(request, 'categoria1.html')