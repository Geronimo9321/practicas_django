from django.urls import path

from . import views

app_name = "genericos"

urlpatterns = [
   path('Rubros/', views.Listar_Rubros, name="path_listar_rubros"), #porque no reconoce esto
]
