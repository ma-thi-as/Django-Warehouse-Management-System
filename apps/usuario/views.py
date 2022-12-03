from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache

from .models import Usuario
from .forms import  FormularioLogin, FormularioUsuario
from .mixins import  LoginAdminMixin
# Create your views here.


class Index(TemplateView):
    template_name = "index.html"


class UsuarioHome(LoginAdminMixin,TemplateView):
    template_name = "usuarios/home.html"

class ListadoUsuario(LoginAdminMixin,ListView):
    model = Usuario
    template_name= 'usuarios/listar.html'
    success_url = reverse_lazy('index')
    paginate_by = 5
    def get_queryset(self):
            
        return self.model.objects.filter(is_active = True)

class RegistrarUsuario(LoginAdminMixin,CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name ='usuarios/crear.html'
    success_url = reverse_lazy('usuario:listar_usuarios')


class UsuarioUpdateView(LoginAdminMixin,UpdateView):
    model = Usuario
    template_name = "usuarios/crear.html"
    form_class = FormularioUsuario
    success_url = reverse_lazy('usuario:listar_usuarios')



class Login(FormView):
    template_name = 'usuarios/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
    
            return HttpResponseRedirect(self.get_success_url())
        else:

            return super(Login,self).dispatch(request,*args,**kwargs)
        
    def form_valid(self, form):
        login(self.request, form.get_user())
        
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/')

