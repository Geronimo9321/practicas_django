from django.urls import path
from . import views

#Como se llama la app
app_name = "comentario"

urlpatterns = [
    path('Agregar/<int:pk>', views.Comentar, name='path_comentar'),
    path('Eliminar/<int:pk>', views.Eliminar.as_view(), name='path_eliminar_comentario')
]