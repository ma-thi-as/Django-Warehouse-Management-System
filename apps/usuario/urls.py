from django.urls import path
from .views import RegistrarUsuario,UsuarioUpdateView, ListadoUsuario, UsuarioHome
urlpatterns = [
    path('',UsuarioHome.as_view(), name = 'home'),
    path('registrar/',RegistrarUsuario.as_view(), name = 'crear_usuarios'),
    path('listar/',ListadoUsuario.as_view(), name = 'listar_usuarios'),
    path('actualizar/<str:pk>',UsuarioUpdateView.as_view(), name = 'actualizar_usuario'),
]