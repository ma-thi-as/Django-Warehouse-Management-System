from django.db import models

# Create your models here.

class Unidad_Medida(models.Model):
    """Model definition for Unidad_Medida."""
    # TODO: Define fields here
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Unidad de medida', max_length=50, unique=True)
    estado = models.BooleanField(default= True)

    class Meta:
        """Meta definition for Unidad_Medida."""

        verbose_name = 'Unidad Medida'
        verbose_name_plural = 'Unidad Medidas'

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    """Model definition for Categoria."""
    # TODO: Define fields here
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Categoria', max_length=50, unique=True)
    estado = models.BooleanField(default= True)

    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    """Model definition for Producto."""

    # TODO: Define fields here
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name = 'Categoria del producto')
    unidad = models.ForeignKey(Unidad_Medida, on_delete=models.CASCADE, verbose_name = 'Unidad de medida del producto')
    nombre = models.CharField('Nombre del producto', max_length=100, blank=False, null=False)
    precio = models.PositiveIntegerField(default=0)
    detalle = models.TextField('Descripcion', max_length=100, blank=False, null=False)
    estado = models.BooleanField('Estado interno del producto',default=True)

    class Meta:
        """Meta definition for Producto."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre
