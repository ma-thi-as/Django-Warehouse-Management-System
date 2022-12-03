from django.urls import path
from .views import (ProveedorHome,ProveedorCreateView,
ProveedorListView,ProveedorUpdateView, ProveedorDeleteView, ProveedorActivo)
urlpatterns = [
    path('',ProveedorHome.as_view(), name = 'home'),
    path('registrar/',ProveedorCreateView.as_view(), name = 'crear_proveedores'),
    path('listar/',ProveedorListView.as_view(), name = 'listar_proveedores'),
    path('actualizar/<str:pk>',ProveedorUpdateView.as_view(), name = 'actualizar_proveedores'),
    path('en_uso/>',ProveedorActivo.as_view(), name = 'estado_activo'),
    path('eliminar/<str:pk>',ProveedorDeleteView.as_view(), name = 'eliminar_proveedores'),

]