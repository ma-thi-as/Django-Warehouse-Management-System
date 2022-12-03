from django.urls import path

from .views import InvetarioListView, InventarioCreateView, InventarioUpdateView, reporteInventarioView
urlpatterns = [
    path('',InvetarioListView.as_view(), name = 'listar_inventario'),
    path('crear/',InventarioCreateView.as_view(), name = 'crear_inventario'),
    path('actualizar/<int:pk>',InventarioUpdateView.as_view(), name = 'actualizar_inventario'),
    path('reporte/', reporteInventarioView.as_view(), name= 'reporte'),

    
]