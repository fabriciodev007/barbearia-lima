from django.urls import path
from .views import IndexView, SobreView,  ContatoView

urlpatterns = [
    path('inicio/', IndexView.as_view(), name='paginas-index'),
    path('sobre/', SobreView.as_view(), name='paginas-sobre'),
    path('contato/', ContatoView.as_view(), name='paginas-contato'),
    
]
