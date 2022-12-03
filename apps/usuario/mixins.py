from django.shortcuts import redirect
from django.urls import reverse_lazy


class LoginAdminMixin(object):    
    def dispatch(self, request, *args, **kwargs):
        """ Sobre escribimos el dispatch con la finalidad de
        Validar si el usuario inicio sesión y si es asi validar cargo.
        Si posee el cargo lo deja continuar la solucitud. 
        Si no redirecciona al index. """
        if request.user.is_authenticated:
            cargo_usuario = request.user.cargo
            if cargo_usuario == 'ADMIN':
                return super().dispatch(request, *args, **kwargs)
        return redirect('index')

class LoginOperdaorMixin(object):    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            cargo_usuario = request.user.cargo
            if cargo_usuario == 'OPERADOR':
                return super().dispatch(request, *args, **kwargs)
        return redirect('index')


class LoginOperadoryAdminMixin(object):
   def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            cargo_usuario = request.user.cargo
            if cargo_usuario == 'OPERADOR' or cargo_usuario == 'ADMIN':
                return super().dispatch(request, *args, **kwargs)
        return redirect('index')    

#Se pueden añadir los permisos requeridos y luego solo se importa en la vista
class ValidarPermisosRequeridosMixin(object):
    permission_required = ''
    url_redirect = None

    def get_perms(self):
        if isinstance(self.permission_required,str):
            return (self.permission_required)
        else:
            return self.permission_required
    
    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('login')
        return self.url_redirect        
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        return redirect(self.get_url_redirect())