from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, ListView
from django.urls import reverse_lazy

from apps.proveedor.models import Proveedor
from apps.proveedor.forms import ProveedorAdminForm, ProveedorForm
from apps.usuario.models import Usuario
from apps.usuario.mixins import LoginAdminMixin

# Create your views here.


class ProveedorHome(LoginAdminMixin,TemplateView):
    template_name = "proveedores/home.html"


class ProveedorActivo(LoginAdminMixin,TemplateView):
    template_name = "components/estado_activo.html"
    success_url = reverse_lazy('proveedor:listar_proveedores')

class ProveedorListView(LoginAdminMixin,ListView):
    model = Proveedor
    template_name = "proveedores/listar.html"
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.filter(estado = True)

class ProveedorCreateView(LoginAdminMixin,CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = "proveedores/crear.html"
    success_url = reverse_lazy('proveedor:listar_proveedores')    


class ProveedorUpdateView(LoginAdminMixin,UpdateView):
    model = Proveedor
    form_class = ProveedorAdminForm
    template_name = "proveedores/actualizar.html"
    success_url = reverse_lazy('proveedor:listar_proveedores')



class ProveedorDeleteView(LoginAdminMixin,DeleteView):
    model = Proveedor
    template_name = 'proveedores/proveedor_confirm_delete.html'
    success_url = reverse_lazy ('proveedor:listar_proveedores')
    
    def post(self, request, pk,*args, **kwargs):
        """Redifinicion metodo post del delelte view
        comprobamos si el objeto proveedor esta en uso.
        Si es asi retornamos una pagina de error.
        En caso de no estar en uso, se elimina de manera logica"""
        proveedor = self.model.objects.get(rut=pk)
        proveedor.estado = False
        proveedor.save()
        return redirect('proveedor:listar_proveedores')