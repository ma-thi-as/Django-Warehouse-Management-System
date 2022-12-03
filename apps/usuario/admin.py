from django.contrib import admin

# Register your models here.

from .models import Usuario

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):

    search_fields = ['nombre','apellido','rut',]
    list_display = ('rut','nombre','apellido','cargo',)
    
admin.site.register(Usuario, UsuarioAdmin)