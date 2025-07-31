from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto

# Create your models here.

class Comentario(models.Model):
    creado = models.DateTimeField(
        auto_now_add=True
    )

    modificado = models.DateTimeField(
        auto_now=True
    )
    texto =models.TextField()
    usuario =models.ForeignKey(User, on_delete=models.CASCADE)
    producto =models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto 