from django.contrib import admin
from apps.proveedor.models import Proveedor
# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
    '''Admin View for Proveedor'''
    list_display = ('nombre','apellido','rut','email',)
    search_fields = ('rut','email','nombre','apellido',)
    ordering = ('rut',)
    
admin.site.register(Proveedor, ProveedorAdmin)