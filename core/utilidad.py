from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_a_pdf(template_src,context_dict = {}):
    """Renderizacion de html a PDF document
    Args:
        template(str): Ruta del template indicado en vista 
        html(dict): renderiza a html los objetos del contexto
        resultado: Inicializamos BytesIO
        pdf = Generamos el documento pdf en base al html permiso de muestra de caracteres especiales
    Returns:
    html como pdf
    """
    template = get_template(template_src)
    html = template.render(context_dict)
    resultado = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),resultado)
    if not pdf.err:
        return HttpResponse(resultado.getvalue(), content_type='application/pdf')
    return None
