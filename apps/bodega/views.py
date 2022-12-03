from django.http import HttpResponse
from django.views.generic import ListView, CreateView, View, UpdateView
from django.urls import reverse_lazy

# Create your views here.
from .models import Inventario
from .forms import InventarioForm



from core.utilidad import render_a_pdf


class InventarioCreateView(CreateView):
    model = Inventario
    form_class = InventarioForm
    template_name = "bodega/crear.html"
    success_url = reverse_lazy('bodega:listar_inventario')


class InventarioUpdateView(UpdateView):
    model = Inventario
    form_class = InventarioForm
    template_name = "bodega/crear.html"
    success_url = reverse_lazy('bodega:listar_inventario')


class InvetarioListView(ListView):
    model = Inventario.history.model
    template_name = 'bodega/listar.html'
    paginate_by = 15

    def get_queryset(self):
        return self.model.objects.all()


class reporteInventarioView(View):
    def get(self, request,*args,**kwargs):
        template_name = "bodega/reporte_inventario.html"
        stock = Inventario.objects.all()
        history = Inventario.history.model
        def his():
            return history.objects.all()

        data = {
            'history': his,
            'productos': stock,
        }
        pdf = render_a_pdf(template_name, data)
        return HttpResponse(pdf, content_type='application/pdf')