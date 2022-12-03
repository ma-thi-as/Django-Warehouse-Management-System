from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import redirect


from .models import Categoria, Producto, Unidad_Medida
from .forms import CategoriaForm, ProductoForm, Unidad_MedidaForm
from apps.usuario.mixins import LoginAdminMixin, LoginOperdaorMixin

#Vistas del producto
class ProductoHome(TemplateView):
    template_name = "productos/home.html"

class CategoriaActivo(TemplateView):
    template_name = "components/estado_activo.html"

class Unidad_MedidaActivo(TemplateView):
    template_name = "components/estado_activo.html"

class ProveedorActivo(TemplateView):
    template_name = "proveedores/estado_activo.html"

class ListadoProductos(ListView):
    model = Producto
    template_name = "productos/listar.html"
    paginate_by = 5
    def get_queryset(self):
        if not self.request.user.cargo == 'ADMIN':
            return self.model.objects.filter(estado = True)
        return self.model.objects.all()
    
class CrearProducto(CreateView):
    model = Producto
    template_name = "productos/crear.html"
    success_url = reverse_lazy('productos:listar_productos')
    form_class = ProductoForm

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "productos/crear.html"
    success_url = reverse_lazy('productos:listar_productos')
    form_class = ProductoForm

class ProductosDeleteView(DeleteView):
    model = Producto
    template_name = "productos/producto_confirm_delete.html"
    success_url = reverse_lazy("productos:listar_productos")

    def post(self, request, pk, *args,**kwargs):
        objeto = self.model.objects.get(id=pk)
        objeto.estado = False
        objeto.save()
        return redirect('productos:listar_productos')

#Vistas de categoria
class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = "productos/categoria/crear.html"
    success_url = reverse_lazy('productos:listar_categoria')
    form_class = CategoriaForm


class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = "productos/categoria/crear.html"
    success_url = reverse_lazy('productos:listar_categoria')
    form_class = CategoriaForm


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = "productos/categoria/categoria_confirm_delete.html"
    success_url = reverse_lazy("productos:listar_categoria")
    def post(self, request, pk, *args,**kwargs):
        objeto = self.model.objects.get(id=pk)
        objeto.estado = False
        objeto.save()
        return redirect('productos:listar_categoria')


class CategoriaListView(ListView):
    model = Categoria
    template_name = "productos/categoria/listar.html"
    paginate_by = 5
    def get_queryset(self):
        if not self.request.user.cargo == 'ADMIN':
            return self.model.objects.filter(estado = True)
        return self.model.objects.all()

#Vistas de unidad_medida
class Unidad_MedidaCreateView(CreateView):
    model = Unidad_Medida
    template_name = "productos/unidad_medida/crear.html"
    success_url = reverse_lazy('productos:listar_unidad_medida')
    form_class = Unidad_MedidaForm

class Unidad_MedidaUpdatView(UpdateView):
    model = Unidad_Medida
    template_name = "productos/unidad_medida/crear.html"
    success_url = reverse_lazy('productos:listar_unidad_medida')
    form_class = Unidad_MedidaForm


class Unidad_MedidaListView(ListView):
    model = Unidad_Medida
    template_name = "productos/unidad_medida/listar.html"
    paginate_by: 5
    def get_queryset(self):
        if not self.request.user.cargo == 'ADMIN':
            return self.model.objects.filter(estado = True)
        return self.model.objects.all()

class Unidad_MedidaDeleteView(DeleteView):
    model = Unidad_Medida
    template_name = "productos/unidad_medida/unidad_medida_confirm_delete.html"
    success_url = reverse_lazy('productos:listar_unidad_medida')
    def post(self, request, pk, *args,**kwargs):
        objeto = self.model.objects.get(id=pk)
        objeto.estado = False
        objeto.save()
        return redirect('productos:listar_unidad_medida')



