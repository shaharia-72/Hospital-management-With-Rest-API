from django.template.loader import render_to_string
from xhtml2pdf import pisa
import io

def generate_pdf(template_src, context_dict):
    """Generate a PDF from a Django template and return as a file-like object."""
    template_content = render_to_string(template_src, context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(template_content.encode("UTF-8")), result)
    if not pdf.err:
        return result.getvalue()
    return None
