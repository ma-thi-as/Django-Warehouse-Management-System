"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include, re_path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.static import serve



from apps.usuario.views import Index, Login, logoutUsuario
urlpatterns = [
    path('',Index.as_view(),name="index"),
    path('admin/', admin.site.urls),
    path('usuarios/',include(('apps.usuario.urls', 'usuario'))),    
    path('proveedores/',include(('apps.proveedor.urls', 'proveedor'))),    
    path('productos/',include(('apps.producto.urls', 'productos'))),    
    path('inventario/',include(('apps.bodega.urls', 'bodega'))),    
    path('login/',Login.as_view(), name='login'),
    path('logout/',login_required(logoutUsuario), name='logout'),
]

#Configuracion creacion de rutas para imagenes de los modelos
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve,{
        'document_root': settings.MEDIA_ROOT,
    }
)]