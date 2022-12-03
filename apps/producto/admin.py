from django.contrib import admin
from .models import Producto, Categoria, Unidad_Medida
# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('nombre', 'precio',)


admin.site.register(Producto,ProductosAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('nombre',)


admin.site.register(Categoria,CategoriaAdmin)

class UnidadAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('nombre',)


admin.site.register(Unidad_Medida,UnidadAdmin)