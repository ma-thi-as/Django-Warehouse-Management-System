from django.db import models

from simple_history.models import HistoricalRecords

from apps.producto.models import Producto
# Create your models here.


class Inventario(models.Model):
    """Model definition for Inventario."""
   
    class Opcion(models.TextChoices):
        ENTRADAS = 'ENTRADAS','Entradas'
        SALIDAS = 'SALIDAS', 'Salidas'
    # TODO: Define fields here
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    opcion = models.CharField('Opcion', max_length=10,choices=Opcion.choices)
    cantidad = models.PositiveIntegerField('Cantidad de productos')
    history = HistoricalRecords()

    class Meta:
        """Meta definition for Inventario."""
        verbose_name = 'Inventario de producto'
        verbose_name_plural = 'Inventario de productos'

    def __str__(self):
        """Unicode representation of Inventario."""
        return str(self.producto)


