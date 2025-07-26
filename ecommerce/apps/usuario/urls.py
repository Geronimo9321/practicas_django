from django.urls import path
from django.contrib.auth import views as auth
from . import views

app_name = 'usuario'

urlpatterns = [
    path('Registro/', views.RegistroUsuario.as_views(), name='path_registro'),
    path('Login/', auth.LoginView.as_views(template_name='usuario/login.html'), name='path_login'),
    path('Logout/', auth.LogoutView.as_views(), name='path_logout'),
]