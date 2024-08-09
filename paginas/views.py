from django.views.generic import TemplateView

# Create your views here.

class SobreView(TemplateView):
    template_name = "sobre.html"
    
class IndexView(TemplateView):
    template_name = "index.html"
    
class ContatoView(TemplateView):
    template_name = "contato.html"

