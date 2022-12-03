from django import template
register = template.Library()

@register.filter(name = 'subtract')
def subtract(value, arg):
    """
    Formatear el rut dado
    Args:
        value (value(int)): Valor de la entrada de prodcutos
        arg (arg(int)): valor de la salida de prodcutos
    Returns:
        int: cantidad de prodcutos total.
    """
    return value - arg

