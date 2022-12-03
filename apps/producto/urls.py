from django.urls import path
from .views import (ProductoUpdateView, CrearProducto,
ProductosDeleteView, ListadoProductos, CategoriaCreateView,
CategoriaListView, CategoriaUpdateView, CategoriaDeleteView,
Unidad_MedidaCreateView, Unidad_MedidaListView,Unidad_MedidaUpdatView,Unidad_MedidaDeleteView, ProductoHome)

urlpatterns = [
    path('home/',ProductoHome.as_view(), name='home'),
    path('registrar/', CrearProducto.as_view(), name= 'crear_productos'),
    path('actualizar/<int:pk>', ProductoUpdateView.as_view(), name= 'actualizar_productos' ),
    path('eliminar/<int:pk>', ProductosDeleteView.as_view(), name= 'eliminar_productos' ),
    path('listar/', ListadoProductos.as_view(), name= 'listar_productos' ),
    path('registrar_categoria/', CategoriaCreateView.as_view(), name= 'crear_categoria' ),
    path('actualizar_categoria/<int:pk>', CategoriaUpdateView.as_view(), name= 'actualizar_categoria'),
    path('eliminar_categoria/<int:pk>', CategoriaDeleteView.as_view(), name= 'eliminar_categoria'),
    path('listar_categoria/', CategoriaListView.as_view(), name= 'listar_categoria'),
    path('registrar_unidad_medida', Unidad_MedidaCreateView.as_view(), name= 'crear_unidad_medida'),
    path('actualizar_unidad_medida/<int:pk>', Unidad_MedidaUpdatView.as_view(), name= 'actualizar_unidad_medida'),
    path('eliminar_unidad_medida/<int:pk>', Unidad_MedidaDeleteView.as_view(), name= 'eliminar_unidad_medida'),
    path('listar_unidad_medida/', Unidad_MedidaListView.as_view(), name= 'listar_unidad_medida'),


]