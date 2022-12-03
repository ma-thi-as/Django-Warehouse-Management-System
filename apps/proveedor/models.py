from django.db import models

# Create your models here.

class Proveedor(models.Model):
    """Model definition for Proveedor."""
    # TODO: Define fields here
    rut = models.CharField('Rut proveedor', max_length=9, unique=True, blank=False, null=False, primary_key=True)
    nombre = models.CharField('Nombre del proveedor',max_length=100, blank=False, null=False)
    apellido = models.CharField('Apellido Proveedor', max_length=50, blank=False, null=False)
    email = models.EmailField('Correo Proveedor',max_length=100, unique=True, blank=False, null=False)
    detalle = models.TextField('Detalles productos proveeidos por el proveedor',max_length=255, null=False, blank=False)
    estado = models.BooleanField('Estado interno del proveedor',default=True)

    class Meta:
        """Meta definition for Proveedor."""
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        """Unicode representation of Proveedor."""
        return f'{self.nombre} {self.apellido}'
