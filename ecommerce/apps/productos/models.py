from django.db import models
from genericos.models import Rubro

# Create your models here.
class Producto(models.Model):
    creado = models.DateTimeField(
        auto_now_add=True
    )
    modificado = models.DateTimeField(
        auto_now=True
    )
    nombre = models.CharField(max_length=30)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to= 'productos')
    rubro = models.ForeignKey(Rubro, null=True, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre
    
#MIGRACIONES
#PASOS
# 1 - verificar que cambios existen
    # python manage.py makemigrations
# 2 - aplicar los cambios
    # python manage.py migrate