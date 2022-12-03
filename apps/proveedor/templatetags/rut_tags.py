from django import template
register = template.Library()

@register.filter
def rut_format(value, separator="."):
    """
    Formatear el rut dado
    Args:
        value (str): rut dado
        separator (str): Caracter separador cada miles default '.'
    Returns:
        str: Rut formateado
    """

    # Obtener rut y el digito verificador 
    rut, verifier_digit = value[:-1], value[-1]
    try:
        # Le indicamos que foormatee el rut a entero, sin el digito verificador cada mil
        # Ejemplo:  12.234.231 
        rut = "{:,}".format(int(rut))
        # Por si indicamos otro separador ademas de ','
        if separator != ",":
            # Aplicamos el separador indicado en la herencia
            rut = rut.replace(",", separator)
        #Retornamos el rut separado por guion y el digito verificador. Ejemplo:  12.234.231-K
        return "%s-%s" % (rut, verifier_digit)
    except ValueError:
        # Si el RUT no puede ser convertido a int
        raise template.TemplateSyntaxError("El RUT debe ser numerico, para ser formateado.")

