from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from core.models import Lista, Produto, Mercado, Usuario
from core.serializers import ListaSerializer, ProdutoSerializer, MercadoSerializer, UsuarioSerializer

class ListaViewSet(ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer
    
class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
class MercadoViewSet(ModelViewSet):
    queryset = Mercado.objects.all()
    serializer_class = MercadoSerializer
    
class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer